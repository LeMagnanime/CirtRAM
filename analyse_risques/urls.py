from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('vulnerabilite', views.vulnerabilite, name='vulnerabilite'),
    path('exemple', views.exemple, name='exemple'),
]