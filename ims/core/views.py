from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from core.models import StockItem, Order, OrderStockItem, Inventory
from core.constants import TransactionMode, OrderStatus
from django.shortcuts import redirect
from django_filters.views import FilterView
from core.filters import OrderFilter, StockItemFilter
from core.forms import OrderForm
from django.contrib.auth.mixins import LoginRequiredMixin
import json

# Create your views here.


class StockItemListView(LoginRequiredMixin, FilterView):
    model = StockItem
    template_name = "core/stockitem_list.html"
    filterset_class = StockItemFilter


class OrderStockItemView(LoginRequiredMixin, TemplateView):
    template_name = "core/create_order.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["payment_options"] = list(TransactionMode._value2member_map_.keys())
        context["status_options"] = list(OrderStatus._value2member_map_.keys())
        context["stockitem_list"] = StockItem.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        selected_items = json.loads(request.POST["selected_items"])
        
        purchased_stockitems = []
        for key, value in selected_items.items():
            stockitem_id = int(key)
            quantity = value["quantity"]
            purchased_stockitems.append({
                    stockitem_id: quantity
                })
        
        order_data_columns = [
            "customer_name", 
            "customer_number", 
            "mode_of_payment", 
            "amount", 
            "remarks", 
            "status"
        ]
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
    

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_order_valid"] = context["order"].status != OrderStatus.INVALID
        context["orderstockitem_list"] = OrderStockItem.objects.exclude(is_deleted=True).filter(order=context["order"])
        return context
    


class OrderListView(LoginRequiredMixin, FilterView):
    model = Order
    template_name = "core/order_list_v2.html"
    filterset_class = OrderFilter
    ordering = ["-created_on"]


class OrderModifyView(LoginRequiredMixin, TemplateView):
    template_name = "core/edit_order.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        order_obj = Order.objects.get(id=context["pk"])
        context["order"] = order_obj
        context["payment_options"] = list(TransactionMode._value2member_map_.keys())
        context["status_options"] = list(OrderStatus._value2member_map_.keys())
        context["orderstockitem_list"] = OrderStockItem.objects.exclude(is_deleted=True).filter(order=order_obj)
        return context

    def post(self, request, *args, **kwargs):
        purchased_stockitems = []
        for key, value in request.POST.items():
            if "purchase_quantity_" in key and value:
                stockitem_id = key.split("purchase_quantity_")[-1]
                purchased_stockitems.append({
                    stockitem_id: value
                })

        for purchased_stockitem in purchased_stockitems:
            for orderstockitem_obj, quantity in purchased_stockitem.items():
                orderstockitem_obj = OrderStockItem.objects.get(id=stockitem_id)
                orderstockitem_obj.quantity = quantity
                orderstockitem_obj.save()    

        order_data_columns = ["customer_name", "customer_number", "mode_of_payment", "remarks", "status", "amount"]
        order_data = {
            column: request.POST[column] for column in order_data_columns
        }
        order_data["created_by"] = request.user
        Order.objects.filter(pk=kwargs["pk"]).update(**order_data) 
           
        return redirect('core:view_order', pk=kwargs["pk"])


class OrderStockItemDeleteView(View):
    model = OrderStockItem
    
    def get(self, request, *args, **kwargs):
        orderstockitem_obj = OrderStockItem.objects.get(id=kwargs['pk'])
        orderstockitem_obj.is_deleted = True
        orderstockitem_obj.save()

        orderstockitem_obj.order.amount = orderstockitem_obj.order.calculate_amount()
        orderstockitem_obj.order.save()
        return redirect('core:view_order', orderstockitem_obj.order.id)
    


class DashboardView(TemplateView):
    template_name = "core/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        completed_orders = Order.objects.filter(status=OrderStatus.COMPLETED)
        total_sales_done = sum(list(completed_orders.values_list("amount", flat=True)))
        pending_orders = Order.objects.filter(status=OrderStatus.PENDING).count()

        out_of_stock_items = 0
        for item in Inventory.objects.all():
            if item.remaining_quantity <= 0:
                out_of_stock_items += 1

        context["total_completed_orders"] = completed_orders.count()
        context["total_sales_done"] = total_sales_done
        context["pending_orders"] = pending_orders
        context["out_of_stock_items"] = out_of_stock_items

        return context