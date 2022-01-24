from django.test import TestCase
from .models import Ingredient, IngredientTemplate, Recipe


class TestIngredients(TestCase):
    """
    Test the ingredient models Ingredient and IngredientTemplate
    """

    def test_template_str_function_returns_name(self):
        template = IngredientTemplate.objects.create(name='Salt', unit='ml')
        self.assertEqual(str(template), 'Salt')

    def test_ingredient_str_function_returns_name(self):
        ingredient = Ingredient.objects.create(
            name='Salt',
            quantity=5,
            unit='ml'
        )
        self.assertEqual(str(ingredient), 'Salt')

    def test_ingredient_quantity_is_float(self):
        ingredient = Ingredient.objects.create(
            name='Salt',
            quantity=5,
            unit='ml'
        )
        self.assertEqual(ingredient.quantity, 5.0)


class TestRecipe(TestCase):
    """
    Test parts of recipe model
    """
    recipe = Recipe.objects.create(
        name='Test',
        created_by='User',
        description='Just to test the model',
    )
    def test_str_function_returns_name(self):
        self.assertEqual(str(TestRecipe.recipe), 'Test')

    def test_ingredients_is_array(self):
        ingredient = Ingredient.objects.create(
            name='Salt',
            quantity=5,
            unit='ml',
        )
        TestRecipe.recipe.ingredients.add(ingredient)
        self.assertEqual(len(TestRecipe.recipe.ingredients), 1)
    
    def test_ingredients_has_correct_data(self):
        TestRecipe.recipe
        self.assertEquals(TestRecipe.recipe.ingredients[0].name, 'Salt')
