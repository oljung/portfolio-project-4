"""
Modole for controlling the view layar
"""
from django.contrib import messages
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse,
    )
from django.views import View
from django.http import HttpResponseRedirect
from .models import (
    Plan,
    Recipe,
    Ingredient,
    Category,
    ShoppingList,
)
from .forms import (
    PlanForm,
    RecipeForm,
    IngredientTemplateForm,
    IngredientForm,
    ShoppingListForm,
)
from .view_methods import (
    change_active_status,
    get_selected_categories,
    add_to_plan,
    add_category,
    add_ingredients_to_shopping_list,
    filter_recipes,
    filter_ingredient_template
)


# Create your views here.
class PlansPage(View):
    """
    View for the homepage, showing information about
    users plans
    """
    def get(self, request):
        """
        Renders the startpage with plans for logged in user
        """
        plans = Plan.objects.filter(user=self.request.user)

        recipes = Recipe.objects.filter(created_by=str(self.request.user))

        shopping_lists = ShoppingList.objects.filter(user=self.request.user)

        active_plan = None

        if plans:
            query = plans.filter(status=1)
            if query:
                active_plan = query[0]

        return render(
            request,
            'plans.html',
            {
                'plans': plans,
                'active_plan': active_plan,
                'recipes': recipes,
                'shopping_lists': shopping_lists,
            }
        )


# Methods connected to plans
def create_plan(request):
    """
    Method for creating a new plan
    """

    if request.method == 'POST':

        plan_form = PlanForm(data=request.POST)

        if plan_form.is_valid():
            # find currently active plan and
            # change to inactive if one is found
            if plan_form.instance.status == 1:
                change_active_status()

            plan_form.instance.user = request.user
            plan = plan_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Plan created successfully'
            )
            return HttpResponseRedirect(reverse('edit_plan', args=[plan.id]))

    return render(
        request,
        'plan_detail.html',
        {
            'activity': 'create'
        }
    )


def edit_plan(request, plan_id):
    """
    Method for editing a plan
    """
    plan = get_object_or_404(Plan, id=plan_id)
    if request.method == 'POST':
        plan_form = PlanForm(data=request.POST, instance=plan)

        if plan_form.is_valid():
            # find currently active plan and
            # change to inactive if one is found
            if plan_form.instance.status == 1:
                change_active_status()

            plan_form.instance.user = request.user
            plan = plan_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Plan edited successfully'
            )

            return redirect('plans')

    return render(
        request,
        'plan_detail.html',
        {
            'plan': plan,
            'activity': 'edit'
        }
    )


def make_plan_active(request, plan_id):
    """
    Method for changing status on a plan to active
    """
    plan = get_object_or_404(Plan, id=plan_id)

    change_active_status()

    plan.status = 1
    plan.save()
    messages.add_message(
        request,
        messages.SUCCESS,
        'Plan successfully activated'
    )

    return redirect('plans')


def remove_recipe_from_plan(request, plan_id):
    """
    Deletes a recipe item from plan
    """
    plan = get_object_or_404(Plan, id=plan_id)
    if request.method == 'POST':
        recipe_list = request.POST.getlist('recipe')

        if recipe_list:
            for recipe in recipe_list:
                recipe_to_remove = get_object_or_404(Recipe, id=recipe)
                plan.recipes.remove(recipe_to_remove)
        messages.add_message(
            request,
            messages.WARNING,
            'Recipes removed successfully'
        )
        return HttpResponseRedirect(reverse('edit_plan', args=[plan_id]))

    return render(
        request,
        'plan_detail.html',
        {
            'plan': plan,
            'activity': 'edit',
        }
    )


def delete_plan(request, plan_id):
    """
    Deletes a plan
    """
    plan = get_object_or_404(Plan, id=plan_id)

    plan.delete()
    messages.add_message(
        request,
        messages.WARNING,
        'Plan deleted successfully'
    )

    return redirect('plans')


class LandingPage(View):
    """
    Landing page for users who are unregistered or not logged in
    """
    def get(self, request):
        """
        Renders the site's landing page
        """
        return render(request, 'index.html')


class RecipeList(View):
    """
    Classes for displaying recipe list and adding recipes to plan
    """
    def get(self, request, plan_id):
        """
        Method for displaying recipelist
        """
        plan = get_object_or_404(Plan, id=plan_id)
        categories = Category.objects.all()
        query = request.GET
        user = request.user
        recipes = filter_recipes(query, user)

        return render(
            request,
            'recipe_list.html',
            {
                'plan': plan,
                'categories': categories,
                'recipes': recipes,
            }
        )

    def post(self, request, plan_id):
        """
        Method for adding recipes to a plan
        """
        plan = get_object_or_404(Plan, id=plan_id)
        recipe_list = request.POST.getlist('recipes')

        if recipe_list:
            for recipe in recipe_list:
                recipe_to_add = get_object_or_404(Recipe, id=recipe)
                plan.recipes.add(recipe_to_add)
        messages.add_message(
            request,
            messages.SUCCESS,
            'Recipes added successfully'
        )

        return HttpResponseRedirect(reverse('edit_plan', args=[plan_id]))


def create_recipe(request, plan_id):
    """
    View for creating recipe, can be used from edit plan or
    from start page, if used from edit plan it will automatically
    add it to the plan
    """
    categories = Category.objects.all()
    if request.method == 'POST':
        recipe_form = RecipeForm(data=request.POST)
        recipe_form.instance.created_by = str(request.user)
        print(recipe_form.is_valid())
        if recipe_form.is_valid():
            recipe = recipe_form.save()
            query_set = request.POST.getlist('category')
            print(recipe.id)
            if query_set:
                add_category(query_set, recipe.id)
            messages.add_message(
                request,
                messages.SUCCESS,
                'Recipe created successfully'
            )
            return HttpResponseRedirect(
                reverse(
                    'edit_recipe',
                    args=[recipe.id, plan_id],
                )
            )

    return render(
        request,
        'recipe_details.html',
        {
            'categories': categories,
            'activity': 'create',
            'plan_id': plan_id,
        }
    )


def edit_recipe(request, recipe_id, plan_id):
    """
    Edits a recipe, and if newly created adds it to plan
    if created from a plan_detail
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    categories = Category.objects.all()
    selected_categories = get_selected_categories(recipe.categories)

    if request.method == 'POST':
        recipe_form = RecipeForm(data=request.POST, instance=recipe)
        recipe_form.instance.created_by = str(request.user)
        if recipe_form.is_valid():
            recipe = recipe_form.save()
            query_set = request.POST.getlist('category')
            if query_set:
                add_category(query_set, recipe_id)

            add_to_plan(recipe, plan_id)

            return redirect('plans')
        messages.add_message(
            request,
            messages.SUCCESS,
            'Recipe edited successfully'
        )
    return render(
        request,
        'recipe_details.html',
        {
            'recipe': recipe,
            'categories': categories,
            'selected_categories': selected_categories,
            'activity': 'edit',
            'plan_id': plan_id,
        }
    )


def view_recipe(request, recipe_id):
    """
    View a recipe without the ability to edit it
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    categories = Category.objects.all()
    selected_categories = get_selected_categories(recipe.categories)

    return render(
        request,
        'recipe_details.html',
        {
            'recipe': recipe,
            'categories': categories,
            'selected_categories': selected_categories,
            'activity': 'view'
        }
    )


def add_ingredient(request, recipe_id, plan_id):
    """
    Method used for adding ingredients to an ingredient list
    in either a recipe or a shopping list
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        ingredient_form = IngredientForm(data=request.POST)
        if ingredient_form.is_valid():
            ingredient = ingredient_form.save()
            recipe.ingredients.add(ingredient)
            recipe.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Ingredient added successfully'
            )
            return HttpResponseRedirect(
                reverse('edit_recipe', args=[recipe_id, plan_id])
            )
    return HttpResponseRedirect(
        reverse('ingredient_list', args=[recipe_id, plan_id])
    )


def remove_ingredient_from_recipe(request, recipe_id):
    """
    Removes ingredients from recipe and then deletes
    that ingredient from the database
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    categories = Category.objects.all()
    plan_id = 0
    if request.method == 'POST':
        ingredient_list = request.POST.getlist('ingredient')

        if ingredient_list:
            for ingredient in ingredient_list:
                ingredient_remove = get_object_or_404(
                    Ingredient,
                    id=ingredient
                )
                recipe.ingredients.remove(ingredient_remove)
                ingredient_remove.delete()
                messages.add_message(
                    request,
                    messages.WARNING,
                    'Ingredients removed successfully'
                )
        return HttpResponseRedirect(
            reverse('edit_recipe', args=[recipe_id, 0])
        )

    return render(
        request,
        'recipe_details.html',
        {
            'recipe': recipe,
            'categories': categories,
            'plan_id': plan_id,
            'activity': 'create'
        }
    )


def recipe_favourites(request, recipe_id):
    """
    Toggles a recipe as marked as favourite for user
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if recipe.favourites.filter(id=request.user.id).exists():
        recipe.favourites.remove(request.user)
    else:
        recipe.favourites.add(request.user)

    return HttpResponseRedirect(
        reverse('plans')
    )


class IngredientTemplateList(View):
    """
    Views the ingredient templates used to add ingredients to a recipe
    """
    def get(self, request, recipe_id, plan_id):
        """
        Views a list of ingredient templates to use for adding ingredients
        to a recipe
        """
        recipe = get_object_or_404(Recipe, id=recipe_id)
        query = request.GET
        ingredient_templates = filter_ingredient_template(query)

        return render(
            request,
            'ingredient_list.html',
            {
                'recipe': recipe,
                'ingredient_templates': ingredient_templates,
                'plan_id': plan_id,
            }
            )

    def post(self, request, recipe_id, plan_id):
        """
        post method is used to create new ingredient templates
        """
        template_form = IngredientTemplateForm(data=request.POST)
        if template_form.is_valid():
            template_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Ingredient created successfully'
            )
        return HttpResponseRedirect(
            reverse('ingredient_list', args=[recipe_id, plan_id])
        )


class ShoppingListView(View):
    """
    View for shopping list
    """
    def get(self, request, list_id):
        """
        Renders the shopping list for selected item
        """
        shopping_list = get_object_or_404(ShoppingList, id=list_id)

        return render(
            request,
            'shopping_list.html',
            {
                'shopping_list': shopping_list
            }
        )

    def post(self, request, list_id):
        """
        Adds an ingredient to a shopping list from the list page
        """
        shopping_list = get_object_or_404(ShoppingList, id=list_id)

        form = IngredientForm(data=request.POST)

        if form.is_valid():
            ingredient = form.save()
            shopping_list.ingredient_list.add(ingredient)
            shopping_list.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Ingredient added successfully'
            )

        return HttpResponseRedirect(
            reverse('shopping_list', args=[list_id])
        )


def create_shopping_list(request, plan_id):
    """
    Creates a shopping list from plan recipes and
    redirects to shopping list url
    """
    if request.method == 'POST':
        list_form = ShoppingListForm(data=request.POST)
        if list_form.is_valid():
            list_form.instance.user = request.user
            shopping_list = list_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Shooping list created successfully'
            )

            add_ingredients_to_shopping_list(shopping_list.id, plan_id)

            return HttpResponseRedirect(
                reverse('shopping_list', args=[shopping_list.id])
            )
    return redirect('plans')


def delete_shopping_list_ingredient(request, list_id, ingredient_id):
    """
    This will remove an ingredient item from a shopping list
    and then delete it from the database
    """
    shopping_list = get_object_or_404(ShoppingList, id=list_id)
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)

    shopping_list.ingredient_list.remove(ingredient)

    ingredient.delete()
    messages.add_message(
        request,
        messages.WARNING,
        'Ingredient removed successfully'
    )

    return HttpResponseRedirect(
            reverse('shopping_list', args=[list_id])
        )


def delete_shopping_list(request, list_id):
    """
    Deletes a shopping lsit after deleting all
    ingredients in list
    """
    shopping_list = get_object_or_404(ShoppingList, id=list_id)

    for ingredient in shopping_list.ingredient_list.all():
        ingredient.delete()

    shopping_list.delete()
    messages.add_message(
        request,
        messages.WARNING,
        'Shooping list deleted successfully'
    )

    return redirect('plans')


class AboutPage(View):
    """
    View for the about page
    """
    def get(self, reqeust):
        """
        Renders the about page
        """
        return render(reqeust, 'about.html')
