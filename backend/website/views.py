from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, CreateCustomerForm
from .models import Customer

# Create your views here.
def home(request):
    customers = Customer.objects.all()

    # Check to see if logging in
    username = password = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('home')
    else:
        return render(request, 'home.html', {'customers': customers})

def logout_user(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You are now registered and logged in')
            return redirect('home')
    else:
        form = SignUpForm()
    
    return render(request, 'register.html', {'form': form})

def customer_record(request, id):
    if request.user.is_authenticated:
        # Look up customer with primary key id
        # in the website_customer table
        customer = Customer.objects.get(id=id)
        return render(request, 'customer_record.html', {
            'customer': customer
        })
    else:
        messages.warning(request, 'You must be logged in to view customer records.')
        return redirect('home')
    
def delete_customer(request, id):
    if request.user.is_authenticated:
        delete_customer = Customer.objects.get(id=id)
        delete_customer.delete()
        messages.success(request, f'{delete_customer} record deleted successfully.')
    else:
        messages.warning(request, 'You must be logged in to delete customer records.')
        
    return redirect('home')

def create_customer(request):
    if request.user.is_authenticated:
        form = CreateCustomerForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                create_customer = form.save()
                messages.success(request, f'Customer {create_customer} created successfully.')
                return redirect('home')

        return render(request, 'create_customer.html', {'form': form})
    else:
        messages.warning(request, 'You must be logged in to create customer records.')
        return redirect('home')
