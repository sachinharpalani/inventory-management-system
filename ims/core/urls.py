from django.urls import path
from core.views import (
    StockItemListView, 
    OrderStockItemView, 
    OrderDetailView,
    OrderListView,
    OrderModifyView
)

urlpatterns = [
    path('stockitem_list', StockItemListView.as_view(), name="stockitem_list"),
    path(
        'order/create', 
        OrderStockItemView.as_view(), 
        name="create_order"
    ),
    path('order/<str:pk>', OrderDetailView.as_view(), name='view_order'),
    path('order_list/', OrderListView.as_view(), name='order_list'),
    path(
        'order/<str:pk>/modify', 
        OrderModifyView.as_view(), 
        name="modify_order"
    ),
    
]