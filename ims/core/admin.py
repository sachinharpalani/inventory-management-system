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
    pass


@admin.register(StockItem)
class StockItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    raw_id_fields = ("items",)
    
    def get_form(self, request, obj=None, **kwargs):
        form = super(OrderAdmin, self).get_form(request, obj, **kwargs)

        form.base_fields['created_by'].initial = request.user
        form.base_fields['created_by'].disabled = True
        form.base_fields['created_by'].widget.can_add_related = False
        form.base_fields['created_by'].widget.can_change_related = False
        form.base_fields['created_by'].widget.can_delete_related = False
        form.base_fields['created_by'].widget.can_view_related = False
        return form
    


@admin.register(OrderStockItem)
class OrderStockItemAdmin(admin.ModelAdmin):
    list_display = ("order", "stockitem", "quantity", "is_deleted")