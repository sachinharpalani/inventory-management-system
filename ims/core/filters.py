import django_filters
from core.models import Order, StockItem

class OrderFilter(django_filters.FilterSet):

    class Meta:
        model = Order
        fields = {
            'id': ['exact'],
            'status': ['exact'], 
            'customer_name': ['exact'], 
            'customer_number': ['exact']
        }


class StockItemFilter(django_filters.FilterSet):
    class Meta:
        model = StockItem
        fields = {
            'subgroup__group': ['exact'],
            'subgroup': ['exact'], 
            'name': ['iexact'], 
        }