from django.urls import path
from tkadventure import views


urlpatterns = [
    path('', views.index, name='home'),
    path('tours/', views.tour_list, name='tours'),
    path('contact/', views.contactView, name='contactus'),
    path('tours/<slug:slug>/', views.tour_detail, name='tour_detail'),
]

