from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'board'

urlpatterns = [
    path('new/', views.question_create, name='question_new'),
    path('detail/<int:question_id>/', views.question_detail, name='question_detail'),
    path('delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('edit/<int:question_id>/', views.question_edit, name='question_edit'),

]
