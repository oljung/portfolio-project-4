"""
Modole for controlling the view layar
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
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
        print(plans)

        active_plan = None

        if plans:
            active_plan = plans.filter(status=1)[0]

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
        print(request.user)

        plan_form = PlanForm(data=request.POST)

        if plan_form.is_valid():
            # find currently active plan and
            # change to inactive if one is found
            if plan_form.instance.status == 1:
                active_plan = Plan.objects.filter(status=1)
                if active_plan:
                    active_plan.status = 2
                    active_plan.save()

            plan_form.instance.user = request.user
            plan_form.save()
            return redirect('plans')

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
        print(request.POST)

        if plan_form.is_valid():
            # find currently active plan and
            # change to inactive if one is found
            if plan_form.instance.status == 1:
                active_plan = Plan.objects.filter(status=1)[0]
                if active_plan:
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
