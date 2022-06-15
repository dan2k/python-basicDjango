from django.shortcuts import render
# from django.http import HttpResponse

# Frontend
def index(request):
    # return HttpResponse('My Stock App')
    return render(request, 'frontend/index.html')


def about(request):
    return render(request, 'frontend/about.html')


def contact(request):
    return render(request, 'frontend/contact.html')


# Auth
def login(request):
    return render(request, 'auth/login.html')


def register(request):
    return render(request, 'auth/register.html')
    

#backend
def dashboard(request):
    return render(request, 'backend/dashboard.html')


def product(request):
    return render(request, 'backend/products.html')


def category(request):
    return render(request, 'backend/category.html')
