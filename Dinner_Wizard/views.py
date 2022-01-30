"""
Modole for controlling the view layar
"""
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
    IngredientTemplate,
    Category,
    ShoppingList
)
from .forms import PlanForm, RecipeForm
from .view_methods import (
    change_active_status,
    get_selected_categories,
    add_to_plan,
    add_category,
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
            }
        )


class LandingPage(View):
    """
    Landing page for users who are unregistered or not logged in
    """
    def get(self, request):
        """
        Renders the site's landing page
        """
        return render(request, 'index.html')


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

    return redirect('plans')


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
        recipes = Recipe.objects.all()
        print(request.GET)

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

        return HttpResponseRedirect(reverse('edit_plan', args=[plan_id]))


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
        return HttpResponseRedirect(reverse('edit_plan', args=[plan_id]))

    return render(
        request,
        'plan_detail.html',
        {
            'plan': plan,
            'activity': 'edit',
        }
    )


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
    print(recipe.categories)
    if request.method == 'POST':
        recipe_form = RecipeForm(data=request.POST, instance=recipe)
        recipe_form.instance.created_by = str(request.user)
        if recipe_form.is_valid():
            recipe = recipe_form.save()
            query_set = request.POST.getlist('category')
            if query_set:
                add_category(query_set, recipe_id)
            if plan_id:
                add_to_plan(recipe, plan_id)

        return redirect('plans')

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


def remove_ingredient_from_recipe(request, recipe_id):
    """
    Removes ingredients from recipe
    """
    recipe = get_object_or_404(Recipe(), id=recipe_id)
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


class IngredientTemplateList(View):
    """
    Views the ingredient templates used to add ingredients to a recipe
    """
    def get(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        templates = IngredientTemplate.objects.all()

        render(
            request,
            'ingredient_list.html',
            {
                'recipe': recipe,
                'templates': templates,
            }
            )
