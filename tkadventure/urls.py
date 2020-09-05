from django.urls import path
from tkadventure import views


urlpatterns = [
    path('', views.index, name='home'),
    path('tours/', views.tour_list, name='tours'),
    path('searchresults', views.SearchResults.as_view(), name="search_results")
]

