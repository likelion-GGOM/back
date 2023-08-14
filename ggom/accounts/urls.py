from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
]