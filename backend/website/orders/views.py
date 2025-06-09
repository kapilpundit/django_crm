from django.shortcuts import redirect, render
from django.contrib import messages
from website.models import Customer, Order
from .forms import OrderRecordForm

def order_list(request):
    if request.user.is_authenticated:
        orders = Order.objects.all()
        return render(request, 'orders/order_list.html', {'orders': orders})
    else:
        messages.warning(request, 'You must be logged in to view order records.')
        return redirect('home')

def order_record(request, id):
    if request.user.is_authenticated:
        order = Order.objects.get(id=id)
        return render(request, 'orders/order_record.html', {'order': order})
    else:
        messages.warning(request, 'You must be logged in to view order records.')
        return redirect('home')

def delete_order(request, id):
    if request.user.is_authenticated:
        delete_order = Order.objects.get(id=id)
        delete_order.delete()
        messages.success(request, f'Order # {delete_order} deleted successfully.')
        return redirect('order-list')
    else:
        messages.warning(request, 'You must be logged in to delete order records.')
        return redirect('home')

def edit_order(request, id):
    if request.user.is_authenticated:
        order = Order.objects.get(id=id)
        form = OrderRecordForm(request.POST or None, instance = order)
        return render(request, 'orders/edit_order.html', {
            'order': order,
            'form': form
            })
    else:
        messages.warning(request, 'You must be logged in to edit order records.')
        return redirect('home')

def update_order(request, id):
    if request.user.is_authenticated:
        order = Order.objects.get(id=id)

        if request.method == 'POST':
            form = OrderRecordForm(request.POST or None, instance = order)

            if form.is_valid():
                update_order = form.save()
                messages.success(request, f'Order # {update_order} updated successfully.')
                return redirect('order-record', id=order.id)
    else:
        messages.warning(request, 'You must be logged in to edit order records.')
        return redirect('home')