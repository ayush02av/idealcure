from django.urls import path

from .views_general import *
from .views_user import *
from .views_dashboard import *

urlpatterns = [
    path('', index.as_view()),

    path('terms', terms.as_view()),
    path('privacy', privacy.as_view()),

    path('treatment/<str:treatment>/', treatment.as_view()),
    path('treatments/', treatments.as_view()),
    path('plans/', plans.as_view()),
    path('consultation/', consultation.as_view()),

    path('profile/', profile.as_view()),
    path('logout/', logout.as_view()),
    path('login/', login.as_view()),

    path('testing/', testing),
    
    path('dashboard/', dashboard.as_view()),
    path('dashboard/ongoingtreatments/', dashboard_ongoing_treatments.as_view()),
    path('dashboard/pendingslots/', dashboard_pending_slots.as_view()),
]