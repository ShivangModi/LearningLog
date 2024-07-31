"""Defines URL patterns for users"""

from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    
    # path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html', next_page=None), name='logout'),

    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Registration page.
    path('register/', views.register, name='register'),
]