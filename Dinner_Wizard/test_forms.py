"""
Module for testing forms
"""
from django.test import TestCase
from .forms import (
    IngredientForm,
    IngredientTemplateForm,
    PlanForm,
    RecipeForm,
    ShoppingListForm
)


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

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test to make sure the metaclass has the necessary fields
        """
        form = IngredientForm()
        self.assertEqual(form.Meta.fields, ['name', 'quantity', 'unit'])


class TestIngredientTemplateForm(TestCase):
    """
    Test the form for ingredient templates
    """
    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test to make sure the metaclass has the necessary fields
        """
        form = IngredientTemplateForm()
        self.assertEqual(form.Meta.fields, ['name', 'unit'])

    def form_has_correct_requirements(self):
        """
        Test that form is invalid if data is missing
        """
        form = IngredientTemplateForm({'name': 'Salt'})
        self.assertFalse(form.is_valid())
        self.assertIn('unit', form.errors.keys())
        self.assertEqual(form.errors['unit'][0], 'This field is required.')


class TestPlansForm(TestCase):
    """
    Test the plans form
    """
    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test to make sure the metaclass has the necessary fields
        """
        form = PlanForm()
        self.assertEqual(form.Meta.fields, ['name', 'status'])

    def form_has_correct_requirements(self):
        """
        Test that form is invalid if data is missing
        """
        form = PlanForm({'status': 1})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')


class TestRecipeForm(TestCase):
    """
    Test the recipe form
    """
    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test to make sure the metaclass has the necessary fields
        """
        form = RecipeForm()
        self.assertEqual(form.Meta.fields, ['name', 'description'])

    def form_has_correct_requirements(self):
        """
        Test that form is invalid if data is missing
        """
        form = RecipeForm({'name': 'Test'})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(
            form.errors['description'][0], 'This field is required.'
        )


class TestShoppingListForm(TestCase):
    """
    Test the shopping list form
    """
    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test to make sure the metaclass has the necessary fields
        """
        form = ShoppingListForm()
        self.assertEqual(form.Meta.fields, ['name'])

    def form_has_correct_requirements(self):
        """
        Test that form is invalid if data is missing
        """
        form = ShoppingListForm()
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(
            form.errors['name'][0], 'This field is required.'
        )
