from django.urls import path
from tkadventure import views


urlpatterns = [
    path('', views.index, name='home')
]

