from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as dj_login,logout as dj_logout
from django.conf import settings
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
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            dj_login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse("Incorrect user <br><a href=""/"">get to htom page </a>")
    return render(request, 'auth/login.html')


def logout(request):
    dj_logout(request)
    return redirect('login')
    # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def register(request):
    return render(request, 'auth/register.html')
    

#backend
@login_required(login_url='/login')
def dashboard(request):
    return render(request, 'backend/dashboard.html')

@login_required(login_url='/login')
def product(request):

    products=Product.objects.all();
   
    return render(request, 'backend/products.html',{'products':products})

@login_required(login_url='/login')
def category(request):
    return render(request, 'backend/category.html')



