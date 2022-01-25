from django.db import models
from django.contrib.auth.models import User


# Create your models here.

STATUS = ((0, 'Upcoming'), (1, 'Active'), (2, 'Previous'))


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name}'


class IngredientTemplate(models.Model):
    name = models.CharField(max_length=50, unique=True)
    unit = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.CharField(max_length=100)
    description = models.TextField(default='Write your description here')
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipe_ingredients'
    )
    favourites = models.ManyToManyField(
        User,
        related_name='recipe_favourites',
        blank=True
    )
    categories = models.ManyToManyField(
        Category,
        related_name='recipe_categories',
        blank=True
    )

    def __str__(self):
        return f'{self.name}'

    def num_of_ingredients(self):
        return self.ingredients.count()


class Plan(models.Model):
    name = models.CharField(max_length=100)
    recipes = models.ManyToManyField(Recipe, related_name='dinner_recipes')
    status = models.IntegerField(choices=STATUS, default=0)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='dinner_plan'
    )

    def __str__(self):
        return f'{self.name}'

    def num_of_recipes(self):
        return self.recipes.count()


class ShoppingList(models.Model):
    name = models.CharField(max_length=100)
    ingredient_list = models.ManyToManyField(
        Ingredient,
        related_name='shopping_ingredients'
    )
    
    def __str__(self):
        return f'{self.name}'

    def num_of_ingredients(self):
        return self.ingredient_list.count()
