"""
Contains functions for handling view logic
"""
from django.shortcuts import get_object_or_404
from .models import (
    Plan,
    Category,
    Recipe,
    ShoppingList,
    Ingredient,
    IngredientTemplate
)


def change_active_status():
    """
    Method for changing a plan status from active to previous
    """
    query = Plan.objects.filter(status=1)

    if query:
        plan = query[0]
        plan.status = 2
        plan.save()


def add_to_plan(recipe, plan_id):
    """
    Adds a newly created recipe to the desired plan
    """

    query = Plan.objects.filter(id=plan_id)

    if query:
        plan = query[0]

        if recipe not in plan.recipes.all():
            plan.recipes.add(recipe)
            plan.save()


def add_category(query_set, recipe_id):
    """
    Adds categories to recipe
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)

    for item in query_set:
        category = get_object_or_404(Category, id=item)
        recipe.categories.add(category)


def get_selected_categories(queryset):
    """
    Returns an array of integers from ids of selected categories
    """
    categories = Category.objects.all()

    selected_categories = []

    for category in categories.all():
        if queryset.filter(id=category.id).exists():
            selected_categories.append(category.id)

    return selected_categories


def add_ingredients_to_shopping_list(list_id, plan_id):
    """
    Adds ingredients to a shopping list from a plan's recipes
    if ingredient appears mutliple, quantity is added instead
    """
    s_list = get_object_or_404(ShoppingList, id=list_id)
    plan = get_object_or_404(Plan, id=plan_id)

    for recipe in plan.recipes.all():
        print(recipe)
        for ingredient in recipe.ingredients.all():
            if s_list.ingredient_list.filter(name=ingredient.name).exists():
                list_ingredient = s_list.ingredient_list.filter(
                    name=ingredient.name
                )[0]
                list_ingredient.quantity += ingredient.quantity
                list_ingredient.save()
            else:
                to_add = Ingredient.objects.create(
                    name=ingredient.name,
                    quantity=ingredient.quantity,
                    unit=ingredient.unit
                )
                s_list.ingredient_list.add(to_add)


def filter_recipes(query):
    """
    Filters recipe list using query from filter form
    """
    recipes = Recipe.objects.all()

    if 'name' in query:
        recipes = recipes.filter(name__icontains=query['name'])

    if 'my-recipes' in query:
        recipes = recipes.filter(created_by=reqeust.user)

    if 'category' in query:
        if int(query['category']) != 0:
            recipes = recipes.filter(categories=query['category'])

    return recipes


def filter_ingredient_template(query):
    """
    Filters ingredient templates based on filter form
    """
    templates = IngredientTemplate.objects.all()

    if 'name' in query:
        templates = templates.filter(name__icontains=query['name'])

    return templates
