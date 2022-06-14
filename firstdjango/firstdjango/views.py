from datetime import date
from django.http import HttpResponse
from django.shortcuts import render


# Build paths inside the project like this: BASE_DIR / 'subdir'.


def index(request):
    # return HttpResponse("Welcom to my homepage")
    
    return render(request,'index.html')

def home(request):
    # return HttpResponse("Welcom to my homepage")
    
    return render(request,'home.html')
def contact(request):
    # return HttpResponse("Welcom to my homepage")
    
    return render(request,'contact.html')
def products(request):
    # return HttpResponse("Welcom to my homepage")
    
    return render(request,'products.html')


def about(request):
    return HttpResponse("About")


def search(request,keyword,page):
    return HttpResponse(f'Search for {keyword} page:{page} ')

def maps(request):
    type= request.GET.get('type','hybrid')
    lat=request.GET.get('lat','13.7245601')
    lon=request.GET.get('lon','100.4930241')
    zoom=request.GET.get('z',11)

    return HttpResponse(f'Map type:{type} <br>location: {lat} , {lon}<br>zoom: {zoom}')

def test(request):
    # return HttpResponse("Welcom to my homepage")
    dt=date.today()
    data={
            'site':{'title':'django framework','msg':'Hello python'}, #dictionary
            'color':['red','green','blue'], #list
            'date':dt #object
    }
    return render(request,'test.html',data)