"""
Module for testing database models
"""
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Ingredient, IngredientTemplate, Recipe, Plan, ShoppingList


class TestIngredients(TestCase):
    """
    Test the ingredient models Ingredient and IngredientTemplate
    """

    def test_template_str_function_returns_name(self):
        """
        Test to make sure the __str__ returns the name
        """
        template = IngredientTemplate.objects.create(name='Salt', unit='ml')
        self.assertEqual(str(template), 'Salt')

    def test_ingredient_str_function_returns_name(self):
        """
        Test to make sure the __str__ returns the name
        """
        ingredient = Ingredient.objects.create(
            name='Salt',
            quantity=5,
            unit='ml'
        )
        self.assertEqual(str(ingredient), 'Salt')

    def test_ingredient_quantity_is_float(self):
        """
        Test to make sure quantity is treated as a float regardless
        of input value
        """
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
    def test_str_function_returns_name(self):
        """
        Test to make sure the __str__ returns the name
        """
        recipe = Recipe.objects.create(
            name='Test',
            created_by='User',
            description='Just to test the model',
        )
        self.assertEqual(str(recipe), 'Test')

    def test_ingredients_num_function(self):
        """
        Test number of ingredients function
        """
        recipe = Recipe.objects.create(
            name='Test',
            created_by='User',
            description='Just to test the model',
        )
        ingredient = Ingredient.objects.create(
            name='Salt',
            quantity=5,
            unit='ml',
        )
        recipe.ingredients.add(ingredient)
        self.assertEqual(recipe.num_of_ingredients(), 1)

    def test_ingredients_has_correct_data(self):
        """
        Test ingredient data is correct
        """
        recipe = Recipe.objects.create(
            name='Test',
            created_by='User',
            description='Just to test the model',
        )
        ingredient = Ingredient.objects.create(
            name='Salt',
            quantity=5,
            unit='ml',
        )
        recipe.ingredients.add(ingredient)
        self.assertEqual(
            recipe.ingredients.filter(name='Salt')[0],
            ingredient
        )


class TestPlan(TestCase):
    """
    Test the plan model to assure recipe is added correctly
    """
    def test_plan_status_default_to_0(self):
        """
        Test default value of status
        """
        test_user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        plan = Plan.objects.create(
            name='Test_Plan',
            user=test_user
        )
        self.assertEqual(plan.status, 0)

    def test_plan_num_of_recipies(self):
        """
        Test number of recipes in plan function
        """
        test_user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        plan = Plan.objects.create(
            name='Test_Plan',
            user=test_user
        )
        recipe = Recipe.objects.create(
            name='Test',
            created_by='User',
            description='Just to test the model',
        )
        plan.recipes.add(recipe)

        self.assertEqual(plan.num_of_recipes(), 1)

    def test_str_returns_name(self):
        """
        Test to make sure the __str__ returns the name
        """
        test_user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        plan = Plan.objects.create(
            name='Test_Plan',
            user=test_user
        )
        self.assertEqual(str(plan), 'Test_Plan')

    def test_plan_recipes_hold_correct_data(self):
        """
        Test to check plan has correct data
        """
        test_user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        plan = Plan.objects.create(
            name='Test_Plan',
            user=test_user
        )
        recipe = Recipe.objects.create(
            name='Test',
            created_by='User',
            description='Just to test the model',
        )
        plan.recipes.add(recipe)

        self.assertEqual(
            plan.recipes.filter(name='Test')[0],
            recipe
        )


class TestShoppingList(TestCase):
    """
    test the two functions of ShoppingList model
    """
    def test_str_fucntion_returns_name(self):
        """
        Test to make sure the __str__ returns the name
        """
        shopping_list = ShoppingList.objects.create(name='test_list')
        self.assertEqual(str(shopping_list), 'test_list')

    def test_shopping_list_num_of_ingredients(self):
        """
        Test number of ingredients in shoppinglist
        """
        shopping_list = ShoppingList.objects.create(name='test_list')
        ingredient = Ingredient.objects.create(
            name='Salt',
            quantity=5,
            unit='ml',
        )
        shopping_list.ingredient_list.add(ingredient)
        self.assertEqual(shopping_list.num_of_ingredients(), 1)
