import django_filters
from django_filters import CharFilter, DateFilter
from .models import MobileNumber, Device


class NumbersFilter(django_filters.FilterSet):
    number = CharFilter(field_name='number', lookup_expr='icontains')
    sim = CharFilter(field_name='sim', lookup_expr='icontains')
    event = DateFilter(field_name="event_date")

    # pin = CharFilter(field_name='pin', lookup_expr='icontains')
    # puk = CharFilter(field_name='puk', lookup_expr='icontains')

    class Meta:
        model = MobileNumber
        fields = ['employee', 'tariff', 'date_added',]


class DevicesFilter(django_filters.FilterSet):
    class Meta:
        model = Device
        fields = ['mark', 'model', 'user']

