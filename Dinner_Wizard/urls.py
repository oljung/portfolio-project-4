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
    path('recipe_list/<plan_id>', views.RecipeList.as_view(), name='recipe_list'),
    path(
        'remove_recipe/<plan_id>',
        views.remove_recipe_from_plan,
        name='remove_recipe',
    ),
]
