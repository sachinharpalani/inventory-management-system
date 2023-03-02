from django import forms
from core.models import OrderStockItem, Order
from core.constants import TransactionMode


class OrderStockItemForm(forms.Form):
    customer_name = forms.CharField(max_length=100)
    customer_number = forms.CharField(max_length=10)
    mode_of_payment = forms.ChoiceField(choices=TransactionMode, initial=TransactionMode.UPI)
    remarks = forms.Textarea()
    amount = forms.IntegerField()
    


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"