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
    
