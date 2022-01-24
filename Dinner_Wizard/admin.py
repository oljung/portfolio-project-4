from django.contrib import admin
from .models import Ingredient, IngredientTemplate, Recipe, Plan


admin.site.register(IngredientTemplate)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Plan)
