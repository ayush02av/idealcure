from django.urls import path
from . import adminpanelviews as views

urlpatterns = [
    path('', views.AdminPanelOverviewPage),
]