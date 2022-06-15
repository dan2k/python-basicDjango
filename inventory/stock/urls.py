from django import views
from django.urls import path
from . import views

urlpatterns = [

    # Frontend
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

    # Auth
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),

    #Backend
    path('backend/dashboard', views.dashboard, name='dashboard'),
    path('backend/product', views.product, name='product'),
    path('backend/category', views.category, name='category'),
    path('backend/logout', views.logout, name='logout'),


]
