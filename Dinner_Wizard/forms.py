"""
Module for forms used to create and edit models
"""
from django import forms
from .models import Plan, IngredientTemplate, Ingredient, Recipe


class PlanForm(forms.ModelForm):
    """
    Form for creating and editing Plan model
    """
    class Meta:
        """
        Creates form from ModelForm using Plan model, user field not needed
        as it is set automatically
        """
        model = Plan
        fields = ['name', 'status']


class IngredientTemplateForm(forms.ModelForm):
    """
    Form for saving ingredient templates
    """
    class Meta:
        """
        Form used to save POST request data
        """
        model = IngredientTemplate
        fields = ['name', 'unit']


class IngredientForm(forms.ModelForm):
    """
    Creates a form for ingredient
    """
    class Meta:
        """
        Form used to save POST request data
        """
        model = Ingredient
        fields = ['name', 'quantity', 'unit']


class RecipeForm(forms.ModelForm):
    """
    Creates form for recipe
    """
    class Meta:
        """
        Form used to save POST request data
        """
        model = Recipe
        fields = ['name', 'description']
