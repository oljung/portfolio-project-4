"""
Module for testing forms
"""
from django.test import TestCase
from .forms import IngredientForm


# Create your tests here.
class TestIngredientForm(TestCase):
    """"
    Tests the ingredient form
    """
    def form_has_correct_requirements(self):
        """
        Test that form is invalid if data is missing
        """
