from django.db import models


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
    
    def __str__(self):
        return self.name


class Bookings(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=255)
    tour_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    message = models.TextField(blank=True)
 
    def __str__(self):
        return self.full_name
