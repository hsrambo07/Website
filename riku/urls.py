from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('<str:room_name>/', views.room, name='chat'),

    path('', views.index,name='room'),
]