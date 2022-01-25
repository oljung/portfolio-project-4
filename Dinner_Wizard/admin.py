from django.contrib import admin
from .models import Ingredient, IngredientTemplate, Recipe, Plan, Category


admin.site.register(IngredientTemplate)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Plan)
admin.site.register(Category)
