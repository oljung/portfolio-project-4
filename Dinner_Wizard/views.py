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
from .forms import PlanForm


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
                query = Plan.objects.filter(status=1)
                if query:
                    active_plan = query[0]
                    active_plan.status = 2
                    active_plan.save()

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
                query = Plan.objects.filter(status=1)
                if query:
                    active_plan = query[0]
                    active_plan.status = 2
                    active_plan.save()

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

    query = Plan.objects.filter(status=1)
    if query:
        active_plan = query[0]
        active_plan.status = 2
        active_plan.save()

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
