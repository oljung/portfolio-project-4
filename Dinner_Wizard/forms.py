"""
Module for forms used to create and edit models
"""
from django import forms
from .models import Plan


class PlanForm(forms.ModelForm):
    """
    Form for creating and editing Plan model
    """
    class Meta:
        """
        Creates form from ModelForm using Plan model, user field not needed
        as it is set automatically
        """
        model = Plan
        fields = ['name', 'status']
