from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('backend/', admin.site.urls),
    path('', include('main.urls')),
    path('adminpanel/', include('main.adminpanelurls')),
    path('consultation/', include('consultation.urls'))
]
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
