"""
Module containing app specific urls
"""
from django.urls import path
from . import views


urlpatterns = [
    path('plans/', views.PlansPage.as_view(), name='plans'),
    path('', views.LandingPage.as_view(), name='home'),
    path('create-plan/', views.create_plan, name='create_plan'),
    path('edit-plan/<plan_id>', views.edit_plan, name='edit_plan'),
    path('make_active/<plan_id>', views.make_plan_active, name='make_active'),
    path(
        'recipe_list/<plan_id>',
        views.RecipeList.as_view(),
        name='recipe_list'
    ),
    path(
        'remove_recipe/<plan_id>',
        views.remove_recipe_from_plan,
        name='remove_recipe',
    ),
    path('create-recipe/<plan_id>', views.create_recipe, name='create_recipe'),
    path(
        'edit-recipe/<recipe_id>/<plan_id>',
        views.edit_recipe,
        name='edit_recipe'
    ),
    path(
        'remove_ingredient/<recipe_id>',
        views.remove_ingredient_from_recipe,
        name='remove_ingredient'
    ),
    path(
        'ingredient_list/<recipe_id>/<plan_id>',
        views.IngredientTemplateList.as_view(),
        name='ingredient_list'
    ),
    path(
        'add-ingredient/<recipe_id>/<plan_id>',
        views.add_ingredient,
        name='add_ingredient'
    ),
    path(
        'shopping-list/<list_id>',
        views.ShoppingListView.as_view(),
        name='shopping_list'
    ),
    path(
        'create-shopping-list/<plan_id>',
        views.create_shopping_list,
        name='create_list'
    ),
]
