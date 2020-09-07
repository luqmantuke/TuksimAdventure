import django_filters
from tkadventure.models import *


class TourFilter(django_filters.FilterSet):
    class Meta:
        model = Tour
        fields = ('name', 'tour_type')