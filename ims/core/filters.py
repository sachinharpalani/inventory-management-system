import django_filters
from core.models import Order

class OrderFilter(django_filters.FilterSet):

    class Meta:
        model = Order
        fields = {
            'id': ['exact'],
            'status': ['exact'], 
            'customer_name': ['exact'], 
            'customer_number': ['exact']
        }