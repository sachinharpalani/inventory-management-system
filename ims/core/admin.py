from django.contrib import admin
from core.models import (
    Group, 
    SubGroup, 
    StockItem, 
    Inventory, 
    Order, 
    OrderStockItem
)

# Register your models here.


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(SubGroup)
class SubGroupAdmin(admin.ModelAdmin):
    list_display = ("group", "name")


@admin.register(StockItem)
class StockItemAdmin(admin.ModelAdmin):
    list_display = ("subgroup", "name", "price")


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id","status", "mode_of_payment", "customer_name", "customer_number")
    search_fields = ("id", "customer_name", "customer_number")
    list_filter = ("status", "mode_of_payment")


@admin.register(OrderStockItem)
class OrderStockItemAdmin(admin.ModelAdmin):
    list_display = ("order", "stockitem", "quantity", "is_deleted")
    search_fields = ("order__id", "stockitem__name", "order__customer_number", "order__customer_name")