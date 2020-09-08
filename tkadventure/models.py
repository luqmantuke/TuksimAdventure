from django.db import models
from django.db.models.signals import pre_save
from tuksimadventures.utils import unique_slug_generator

tour_list = [
    ('t', "Trekking"),
    ('s', "Safari"),
    ('i', "Island"),
    ('m', "More")
]


class Tour(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    tour_type = models.CharField(choices=tour_list, max_length=20)
    slug = models.SlugField(max_length=250, blank=True, null=True)
    tour_descr = models.CharField(max_length=1000, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("tour_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


class Bookings(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=255, null=True)
    tour_name = models.CharField(max_length=255, null=True)
    quantity = models.PositiveIntegerField()
    message = models.TextField(blank=True, null=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.full_name


def slug_generator(sender, instance, *args, **kwargs): 
    if not instance.slug: 
        instance.slug = unique_slug_generator(instance) 


pre_save.connect(slug_generator, sender = Tour)

