from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Idealcure Backend'
admin.site.site_title = 'Idealcure Backend'
admin.site.index_title = 'Overview'

urlpatterns = [
    path('backend/', admin.site.urls),
    path('', include('main.urls')),
    path('adminpanel/', include('main.adminpanelurls')),
    path('consultation/', include('consultation.urls'))
]