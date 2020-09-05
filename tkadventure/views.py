from django.shortcuts import render
from django.views.generic import ListView 
from tkadventure.models import Tour
from django.db.models import Q
from tkadventure.filters import TourFilter


def index(request):
    return render(request, 'index.html')


def tour_list(request):
    tours = Tour.objects.all()
    template_name = 'tkadventure/tour_list.html'
    myFilter = TourFilter(request.GET, queryset=tours)
    tours = myFilter.qs
    context = {
        'tour': tours,
        'myfilter': myFilter
    }
    return render(request, template_name, context)




class SearchResults(ListView):
    model = Tour
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Tour.objects.filter(
            Q(tour_type__contains=query)
        )
        return object_list

    