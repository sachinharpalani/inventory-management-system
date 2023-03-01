from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, UpdateView
from core.models import StockItem, Order, OrderStockItem
from core.constants import TransactionMode, OrderStatus
from django.shortcuts import redirect
from django_filters.views import FilterView
from core.filters import OrderFilter
from core.forms import OrderForm

# Create your views here.


class StockItemListView(ListView):
    model = StockItem


class OrderStockItemView(TemplateView):
    template_name = "core/create_order.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["payment_options"] = list(TransactionMode._value2member_map_.keys())
        context["status_options"] = list(OrderStatus._value2member_map_.keys())
        context["stockitem_list"] = StockItem.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        purchased_stockitems = []
        for key, value in request.POST.items():
            if "purchase_quantity_" in key and value:
                stockitem_id = key.split("purchase_quantity_")[-1]
                purchased_stockitems.append({
                    stockitem_id: value
                })
        
        order_data_columns = ["customer_name", "customer_number", "mode_of_payment", "amount", "remarks", "status"]
        order_data = {
            column: request.POST[column] for column in order_data_columns
        }
        order_data["created_by"] = request.user
        order_obj = Order.objects.create(**order_data)
        for purchased_stockitem in purchased_stockitems:
            for stockitem_id, quantity in purchased_stockitem.items():
                stockitem_obj = StockItem.objects.get(id=stockitem_id)
                OrderStockItem.objects.create(**{
                    "stockitem": stockitem_obj,
                    "order": order_obj,
                    "quantity": quantity
                })    
        return redirect('core:view_order', pk=order_obj.id)


class OrderDetailView(DetailView):
    model = Order


# class OrderListView(ListView):
#     model = Order


class OrderListView(FilterView):
    model = Order
    template_name = "core/order_list_v2.html"
    filterset_class = OrderFilter


class OrderModifyView(TemplateView):
    template_name = "core/edit_order.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        order_obj = Order.objects.get(id=context["pk"])
        context["order"] = order_obj
        context["payment_options"] = list(TransactionMode._value2member_map_.keys())
        context["status_options"] = list(OrderStatus._value2member_map_.keys())
        context["stockitem_list"] = OrderStockItem.objects.filter(order=order_obj)
        return context

    def post(self, request, *args, **kwargs):
        order_data_columns = ["customer_name", "customer_number", "mode_of_payment", "remarks", "status"]
        order_data = {
            column: request.POST[column] for column in order_data_columns
        }
        order_data["created_by"] = request.user
        Order.objects.filter(pk=kwargs["pk"]).update(**order_data)    
        return redirect('core:view_order', pk=kwargs["pk"])

    