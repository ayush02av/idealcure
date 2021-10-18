from django.contrib import admin
from django.urls import path, include

from django.conf import settings

admin.site.site_header = 'Idealcure Backend Administration'
admin.site.site_title = 'Idealcure Backend Administration'
admin.site.index_title = 'Overview'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls'))
]
