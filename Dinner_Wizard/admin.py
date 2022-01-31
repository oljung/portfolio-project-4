"""
sends models to admin page
"""
from django.contrib import admin
from .models import (
    Ingredient,
    IngredientTemplate,
    Recipe,
    Plan,
    Category,
    ShoppingList,
)


admin.site.register(IngredientTemplate)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Plan)
admin.site.register(Category)
admin.site.register(ShoppingList)
