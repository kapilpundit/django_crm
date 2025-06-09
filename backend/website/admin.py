from django.contrib import admin
from .models import Customer, Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer_name', 'created_at')

    def customer_name(self, obj):
        return f"{obj.customer.first_name} {obj.customer.last_name}"
    
    customer_name.short_description = 'Customer'

class OrderInline(admin.TabularInline):  # or use StackedInline
    model = Order
    extra = 0  # don't show extra blank forms
    readonly_fields = ('order_number', 'created_at')  # optional

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'email', 'phone', 'city', 'state', 'created_at')
    inlines = [OrderInline]

    def customer_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    
    customer_name.short_description = 'Customer Name'

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)