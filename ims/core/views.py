from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from core.models import StockItem
from core.forms import OrderStockItemForm

# Create your views here.


class StockItemListView(ListView):
    model = StockItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class OrderStockItemView(TemplateView):
    template_name = "common/form.html"