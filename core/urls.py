# Imports
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import (path, include)

# core urls
urlpatterns = [
    # 1. Default Admin
    path('admin/', admin.site.urls),
    #1. Website
    path('', include('apps.website.urls', namespace='website')),
    #2. Accounts
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),  
] 

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT) 
    urlpatterns += static(
        settings.STATIC_URL, 
        document_root = settings.STATIC_ROOT)
        