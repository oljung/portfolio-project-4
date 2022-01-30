"""
Contains functions for handling view logic
"""
from django.shortcuts import get_object_or_404
from .models import Plan, Category, Recipe


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
    plan = get_object_or_404(Plan, id=plan_id)
    
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
