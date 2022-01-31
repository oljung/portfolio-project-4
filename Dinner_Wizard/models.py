"""
Module for handling the database models
"""
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

STATUS = ((0, 'Upcoming'), (1, 'Active'), (2, 'Previous'))


class Ingredient(models.Model):
    """
    Model for the ingredients, used in recipes and shopping list
    """
    name = models.CharField(max_length=50)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10)

    class Meta:
        """
        change ordering of ingredients
        """
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class IngredientTemplate(models.Model):
    """
    Model for ingredient template, for accessing premade ingredients
    """
    name = models.CharField(max_length=50, unique=True)
    unit = models.CharField(max_length=10)

    class Meta:
        """
        change ordering of ingredient templates
        """
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    """
    Model for categories used by recipes for categorizing and easy search
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    """
    Model for the recipes, used by the Plan model
    """
    name = models.CharField(max_length=200)
    created_by = models.CharField(max_length=100)
    description = models.TextField(default='Write your description here')
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipe_ingredients',
        blank=True
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
        """
        Method for quickly determining number of ingredients in recipe
        """
        return self.ingredients.count()


class Plan(models.Model):
    """
    Model for the plan, containing recipes to make a shopping list from
    """
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
        """
        Easy return of total number of recipes
        """
        return self.recipes.count()


class ShoppingList(models.Model):
    """
    Model for the shopping list, created from all ingredients in a plan
    """
    name = models.CharField(max_length=100)
    ingredient_list = models.ManyToManyField(
        Ingredient,
        related_name='shopping_ingredients'
    )

    def __str__(self):
        return f'{self.name}'

    def num_of_ingredients(self):
        """
        Returns total number of ingredients in a shopping list
        """
        return self.ingredient_list.count()
