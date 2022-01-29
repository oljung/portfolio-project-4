from . import views
from django.urls import path


urlpatterns = [
    path('plans/', views.PlansPage.as_view(), name='plans'),
    path('', views.LandingPage.as_view(), name='home'),
    path('create-plan/', views.create_plan, name='create_plan'),
    path('edit-plan/<plan_id>', views.edit_plan, name='edit_plan')
]
