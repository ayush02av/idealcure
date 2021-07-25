from django.urls import path
from . import views

urlpatterns = [
    path('', views.ConsultationPage),
    path('plans/', views.Plans)
]