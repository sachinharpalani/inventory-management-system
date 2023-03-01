from django.urls import path
from core.views import StockItemListView, OrderStockItemView

urlpatterns = [
    path('stockitem_list', StockItemListView.as_view(), name="stockitem_list"),
    path(
    'order_stockitem/', 
    OrderStockItemView.as_view(), 
    name="order_stockitem")
]