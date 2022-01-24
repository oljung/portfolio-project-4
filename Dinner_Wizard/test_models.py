from django.test import TestCase
from .models import Ingredient, IngredientTemplate


class TestIngredients(TestCase):
    """
    Test the ingredient models Ingredient and IngredientTemplate
    """
    
    def test_template_str_function_returns_name(self):
        template = IngredientTemplate.objects.create(name='Salt', unit='ml')
        self.assertEqual(str(template), 'Salt')
    
    def test_ingredient_str_function_returns_name(self):
        ingredient = Ingredient.objects.create(name='Salt', quantity=5, unit='ml')
        self.assertEqual(str(ingredient), 'Salt')
    
    def test_ingredient_quantity_is_float(self):
        ingredient = Ingredient.objects.create(name='Salt', quantity=5, unit='ml')
        self.assertEqual(quantity, 5.0)
