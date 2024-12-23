import debug_toolbar
from django.contrib import admin
from django.urls import include, path

from anfisa_for_friends import settings

urlpatterns = [
    path('', include('homepage.urls')),
    path('about/', include('about.urls')),
    path('ice_cream/', include('ice_cream.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)