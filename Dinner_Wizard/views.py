"""
Modole for controlling the view layar
"""
from django.shortcuts import render
from django.views import View
from .models import (
    Plan,
    Recipe,
    Ingredient,
    IngredientTemplate,
    Category,
    ShoppingList
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
