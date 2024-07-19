from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')


def services(request):
    return render(request, 'services.html')

def application(request):
    return render(request, 'application.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')

def administration(request):
    return render(request, 'administration.html')




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
