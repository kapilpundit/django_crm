from django import forms
from website.models import Order, Customer

# Create Customer Form
class OrderRecordForm(forms.ModelForm):
    order_number = forms.CharField(
        required=True,
        label='',
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Order Number'}
        )
    )

    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        required=True,
        label='',
        widget=forms.Select(
            attrs={'class': 'form-select', 'placeholder': 'Customer'}
        )
    )

    class Meta:
        model = Order
        fields = ['order_number', 'customer']
