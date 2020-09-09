from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from tkadventure.models import *
from django.db.models import Q
from tkadventure.filters import TourFilter
from tkadventure.forms import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from blog.models import Post
from django.core.mail import send_mail, BadHeaderError
from tuksimadventures import settings



def index(request):
    posts = Post.objects.all().order_by('-publish')[0:4]
    tour = Tour.objects.filter(popular=True).order_by('name')[0:8]
    context = {
         'posts': posts,
         'tours': tour
    }
    return render(request, 'index.html', context)


def tour_detail(request, slug):
    q = Tour.objects.filter(slug__iexact = slug)
    book_subject = "Someone just booked a tour man!!"
    if q.exists(): 
        q = q.first()
    else: 
       return render(request, 'tkadventure/404.html', status=404)
    

    if request.method == "POST":

        form = BookingForm(request.POST)
        if form.is_valid():
            book_full_name = form.cleaned_data['full_name']
            book_email = form.cleaned_data['email']
            book_tour_name = form.cleaned_data['tour_name']
            book_quantity = form.cleaned_data['quantity']
            book_message = form.cleaned_data['message']
            book_user_message = f'Customer "{book_full_name}" with the email "{book_email}" just booked a tour to " " "{book_tour_name}" with quantity of " "  {book_quantity} person/people and left a message " " "{book_message}" please contact him as soon as possible'
            form.save()
            try: 
                send_mail(book_subject, book_user_message, settings.EMAIL_HOST_USER, ['lsuleiman2002@gmail.com'], settings.FAIL_SILENTLY)
            
            except BadHeaderError:
                return HttpResponse('Invalid Header.')
            form.save()
            messages.success(request, f'Booking  was successfully we shall contact you shortly {full_name} thank you!')
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

def tour_list(request):
    tours = Tour.objects.all()
    template_name = 'tkadventure/tour_list.html'
    myFilter = TourFilter(request.GET, queryset=tours)
    tours = myFilter.qs
    subject = "Someone just booked a tour."
    
    if request.method == "POST":

        form = BookingForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            tour_name = form.cleaned_data['tour_name']
            quantity = form.cleaned_data['quantity']
            message = form.cleaned_data['message']
            user_message = f'Customer "{full_name}" with the email "{email}" just booked a tour to  "{tour_name}" with quantity of {quantity} person/people and left a message "{message}" please contact him as soon as possible.'
            form.save()
            try:
                send_mail(subject, user_message, settings.EMAIL_HOST_USER, ['joycemollel001@gmail.com'], settings.FAIL_SILENTLY)
            
            except BadHeaderError:
                return HttpResponse('Invalid Header.')
            messages.success(request, f'Tour submition was successfully we shall contact you {full_name} shortly!')

            return HttpResponseRedirect(reverse('home'))
        else:
            print(form.errors)
    else:
        form = BookingForm()

    return render(request, template_name, {'tour': tours,
        'myfilter': myFilter, 'bkform': form})


    

def contactView(request):

    form_class = ContactForm
    # if request is not post, initialize an empty form
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            message = form.cleaned_data['message']
            contact_message = f'Customer  "{name}" with the email {email} just contacted you and left a message  "{message}" please contact him as soon as possible'
            try: 
                send_mail(subject, contact_message, settings.EMAIL_HOST_USER, ['lsuleiman2002@gmail.com'], settings.FAIL_SILENTLY)
            except BadHeaderError:
                return HttpResponse('Invalid Header.')
            
            messages.success(request, f"Thank You For Contacting Us { name }, We will Reach You as fast as we can. :)")
            return HttpResponseRedirect(reverse('home'))
            
        else:
            form = ContactForm()
        
    return render(request, 'contact.html', {'form': form})