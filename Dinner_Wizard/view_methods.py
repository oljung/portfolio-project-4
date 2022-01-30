"""
Contains functions for handling view logic
"""
from django.shortcuts import get_object_or_404
from .models import Plan


def change_active_status():
    """
    Method for changing a plan status from active to previous
    """
    query = Plan.objects.filter(status=1)

    if query:
        plan = query[0]
        plan.status = 2
        plan.save()


def add_to_plan(recipe, plan_id):
    """
    Adds a newly created recipe to the desired plan
    """
    plan = get_object_or_404(Plan, plan_id)

    plan.recipes.add(recipe)
    plan.save()
