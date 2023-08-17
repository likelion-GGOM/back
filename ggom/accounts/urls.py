from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('mypage/', views.mypage, name='mypage'),
    path('change_nickname/', views.change_nickname, name='change_nickname'),
    path('change_profile/', views.change_profile, name='change_profile'),
    path('change_password/', views.change_password, name='change_password'),
]
