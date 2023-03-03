from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from core.constants import OrderStatus, TransactionStatus, TransactionMode

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "group"  


class SubGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.group} | {self.name}"

    class Meta:
        db_table = "subgroup"  


class StockItem(models.Model):
    subgroup = models.ForeignKey(SubGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.subgroup} | {self.name}"

    class Meta:
        db_table = "stockitem"  


class Inventory(models.Model):
    stockitem = models.ForeignKey(StockItem, on_delete=models.CASCADE, related_name="inventory")
    quantity = models.IntegerField()

    @property
    def remaining_quantity(self):
        ordered_items = OrderStockItem.objects.exclude(
            Q(order__status=OrderStatus.INVALID) | Q(is_deleted=True)
        ).filter(stockitem=self.stockitem).values_list("quantity", flat=True)
        used_quantity = sum(list(ordered_items))
        return self.quantity - used_quantity
    
    def __str__(self) -> str:
        return f"{self.stockitem} -> {self.quantity}"

    class Meta:
        db_table = "inventory"  


class Order(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(StockItem, through="OrderStockItem")
    amount = models.IntegerField()
    status = models.CharField(
        max_length=255,
        choices=OrderStatus.choices, 
    )
    mode_of_payment = models.CharField(
        max_length=255,
        choices=TransactionMode.choices
    )
    customer_name = models.CharField(max_length=100, null=True, blank=True)
    customer_number = models.CharField(max_length=10, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id} | {self.status} | {self.customer_name} | {self.customer_number}"

    def calculate_amount(self):
        total_amount = 0
        order_stock_items = OrderStockItem.objects.exclude(is_deleted=True).filter(order=self)
        for obj in order_stock_items:
            total_amount += (obj.stockitem.price * obj.quantity)
        
        return total_amount

    class Meta:
        db_table = "order"  


class OrderStockItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    stockitem = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    quantity = models.IntegerField() 
    is_deleted = models.BooleanField(default=False)

