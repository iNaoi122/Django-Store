"""
Definition of urls for Django_Store.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('store.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)