from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from tkadventure.models import Tour
from django.db.models import Q
from tkadventure.filters import TourFilter
from tkadventure.forms import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages



def index(request):
    return render(request, 'index.html')


def tour_list(request):
    tours = Tour.objects.all()
    template_name = 'tkadventure/tour_list.html'
    myFilter = TourFilter(request.GET, queryset=tours)
    tours = myFilter.qs
    
    if request.method == "POST":

        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Tour submition was successfully!")
            return HttpResponseRedirect(reverse('home'))
        else:
            print(form.errors)
    else:
        form = BookingForm()

    return render(request, template_name, {'tour': tours,
        'myfilter': myFilter, 'bkform': form})

def tour_detail(request, slug):
    q = Tour.objects.filter(slug__iexact = slug)
    if q.exists(): 
        q = q.first()
    else: 
       return render(request, 'tkadventure/404.html', status=404)
    

    if request.method == "POST":

        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Tour submition was successfully!")
            return HttpResponseRedirect(reverse('home'))
        else:
            print(form.errors)
    else:
        form = BookingForm()

    
    context = {
        'tourform': form,
        'tour': q
    }

    return render(request, 'tkadventure/tour_detail.html', context) 
    