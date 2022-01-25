from . import views
from django.urls import path


urlpatterns = [
    path('plans/', views.PlansPage.as_view(), name='plans'),
    path('', views.LandingPage.as_view(), name='home'),
]
