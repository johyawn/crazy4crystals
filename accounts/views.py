from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm  # Remove UserCreationForm import
from .forms import MyUserCreationForm
from .models import Product, MyUser

def home(request):
    user = request.user
    return render(request, 'main.html', {'user': user})
    return HttpResponse('<h1>Hello, john is testing!</h1>')

def my_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'main.html', context)

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def checkout(request):
    # Retrieve cart items from the session or set it to an empty list if it doesn't exist
    cart_items = request.session.get('cart', [])

    if cart_items:
        # Retrieve actual product objects based on cart item IDs
        products_in_cart = Product.objects.filter(id__in=[item['product_id'] for item in cart_items])
        total_amount = sum(item['quantity'] * product.price for item, product in zip(cart_items, products_in_cart))
    else:
        products_in_cart = []
        total_amount = 0

    return render(request, 'checkout.html', {'cart_items': cart_items, 'products_in_cart': products_in_cart, 'total_amount': total_amount})

def signup(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('email')  # Change to 'email' as USERNAME_FIELD is set to 'email'
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=username, password=raw_password)  # Use 'email' as the username field
            print(f"New user signed up: {username}")  # Debug message
            if user is not None:
                print(f"Authentication successful for user: {username}")  # Debug message
                login(request, user)
                print(f"User {username} logged in")  # Debug message
                return redirect('home')  # Redirect to the home page after successful signup
            else:
                print("Authentication failed")  # Debug message
    else:
        form = MyUserCreationForm()  # Correct form instantiation
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
