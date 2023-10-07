from django.shortcuts import render, redirect
from .models import Vehicles, Location, Order
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, OrderForm, ContactForm
from django.utils import timezone
from django.db.models import Q



# Create your views here.

def home(request):
    cars =Vehicles.objects.all()
    orders = Order.objects.all()
    
    if request.method == 'GET':
        for order in orders:
            car = order.car
            if order.endRent <= timezone.now().date():
                car.is_available = True
                car.save()
    
    context = {'cars':cars}
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')

def cars(request):
    orders = Order.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ''
        
    cars = Vehicles.objects.filter(
        Q(car_model__icontains = q) |
        Q(car_brand__icontains = q)
    )
    
    if request.method == 'GET':
        for order in orders:
            car = order.car
            if order.endRent <= timezone.now().date():
                car.is_available = True
                car.save()
            

    context = {'cars':cars}
    return render(request, 'cars.html', context)

def car(request, pk):
    cars = Vehicles.objects.all()
    car = Vehicles.objects.get(id=pk)
    context = {'car':car, 'cars':cars}
    return render(request, 'car-single.html', context)

def book_car(request, pk):
    pickupPlace = Location.objects.all()
    car = Vehicles.objects.get(id=pk)
    form = OrderForm

    if (request.method == 'POST'):
        form = OrderForm(request.POST)
        
        if form.is_valid():
            order = form.save(commit=False)
            order.car = car
            order.price_per_day = car.price
            order.customer = request.user
            order.save()
            
            car.is_available = False
            car.save()
            messages.success(request, 'Congratulations, your order has been successfully placed!')
            return redirect('book-details', pk=order.id)
        else:
            messages.error(request, 'Something went wrong!')
    
        
    context = {"car":car, 'pickupPlace':pickupPlace, 'form':form}
    return render(request, 'book.html', context)

@login_required
def book_details(request, pk):
    order = Order.objects.get(id=pk)
    car = order.car
    
    context = {'order':order, 'car':car}
    return render(request, 'book_details.html', context)

@login_required
def book_confirmation(request, pk):
    order = Order.objects.get(id=pk)
    car = order.car
    
    context = {'order':order, 'car':car, 'page':'confirmation'}
    
    return render(request, 'book_details.html', context)

@login_required
def cancel_booking(request, pk):
    order = Order.objects.get(id=pk)
    car = order.car
    car.is_available = True
    car.save()
    
    order.delete()
    messages.success(request, 'Booking canceled!')
    return redirect('home')

@login_required
def booking_list(request):
    user = request.user
    user_orders = user.order_set.all()
    
    context = {'user':user, 'orders':user_orders}
    return render(request, 'booking_list.html', context)
    

def contact(request):
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Message successfully send!')
            return redirect('contact')
        else:
            messages.error(request, 'Something went wrong!')
            
            
    context = {'form':form}
    return render(request, 'contact.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Wrong password or username!')
    
    context = {'page':'login'}
    return render(request, 'login_register.html', context)

def register(request):
    form = UserRegistrationForm()
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Something went wrong!')
        
    context = {'page':'register', 'form':form}
    return render(request, 'login_register.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

