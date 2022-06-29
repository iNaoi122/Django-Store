"""
Definition of urls for Django_Store.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from store import  views


urlpatterns = [
    path('', include('store.urls')),
    path('admin/', admin.site.urls),
]
