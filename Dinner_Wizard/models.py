from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


# Create your models here.

STATUS = ((0, 'Upcoming'), (1, 'Active'), (2, 'Previous'))


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=10)


class IngredientTemplate(models.Model):
    name = models.CharField(max_length=50, unique=True)
    unit = models.CharField(max_length=10)


class Recipe(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_by = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipe_ingredients'
    )
    favourites = models.ManyToManyField(
        User,
        related_name='recipe_favourites',
        blank=True
    )
    categories = ArrayField(models.IntegerField())


class Plan(models.Model):
    name = models.CharField(max_length=100)
    dinners = ArrayField(models.CharField(max_length=20))
    recipes = models.ManyToManyField(Recipe, related_name='dinner_recipes')
    status = models.IntegerField(choices=STATUS, default=0)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='dinner_plan'
    )


class ShoppingList(models.Model):
    name = models.CharField(max_length=100)
    ingredient_list = models.ManyToManyField(
        Ingredient,
        related_name='shopping_ingredients'
    )
