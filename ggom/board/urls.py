from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'board'

urlpatterns = [
    path('new/', views.question_create,  name='question_new'),
    path('list/', views.question_list, name='question_list'),
    path('mylist/', views.my_question_list, name='my_question_list'),
    path('answerlist', views.my_answer_list, name='my_answer_list'),
    path('detail/<int:question_id>/', views.question_detail, name='question_detail'),
    path('answer/<int:question_id>/', views.answer_create, name='answer_create'),
    path('delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('edit/<int:question_id>/', views.question_edit, name='question_edit'),
]
