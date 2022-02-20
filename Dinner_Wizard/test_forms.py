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
        Test that form is invalid if data is missing, form will
        always have name and unit from template, test makes sure
        a quantity is added
        """
        form = IngredientForm({'name': 'Salt', 'unit': 'ml'})
        self.assertFalse(form.is_valid())
        self.assertIn('quantity', form.errors.keys())
        self.assertEqual(form.errors['quantity'][0], 'This field is required.')
