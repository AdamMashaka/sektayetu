from django.shortcuts import render, redirect
from .forms import UserProfileForm, UserCreationForm
from .models import UserProfile, Blog  # Assuming Blog model is defined elsewhere
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

import random
import string

# Helper function to generate a license number
def generate_license_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

# Registration view for creating a new user
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

# Registration view for creating a user profile
def register_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.license_number = generate_license_number()
            user_profile.save()
            return render(request, 'administration.html', {'license_number': user_profile.license_number})
    else:
        form = UserProfileForm()
    return render(request, 'administration.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('success_page')  # Redirect to a success page, replace 'success_page' with your actual success page name
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'login.html')  # Assuming there's a login.html template

# View functions for other pages
def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog.html', context)

def home(request):
    return render(request, 'index.html')

def index(request):
    context = {}
    return render(request, 'index.html', context)

def administration(request):
    context = {}
    return render(request, 'administration.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})