from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import login_view, registration, services, application, administration




urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('administration/', views.administration, name='administration'),
    path('services/', views.services, name='services'),
    path('application/', views.application, name='application'),
    path('login/', login_view, name='login'),  
    path('register/', views.registration, name='registration'),
    path('administration/', views.administration, name='administration'),
    
]
