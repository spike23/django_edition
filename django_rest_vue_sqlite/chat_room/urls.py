# coding=utf-8
from django.urls import path
from .views import *

urlpatterns = [
    path('room/', Rooms.as_view()),
]