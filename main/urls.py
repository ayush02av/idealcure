from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.HomePage),
    path('treatments/<str:treatmentFor>/', views.TreatmentsPage),
    path('profile/', views.Profile),
    path('profile/<str:username>/', views.ProfilePage),
    path('profile_login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('profile_logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
]