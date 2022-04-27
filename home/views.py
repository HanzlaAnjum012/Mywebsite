from django.shortcuts import render
from home.models import *

# Create your views here.

def home(request):
    home_item = Home.objects.filter(preview=True)
    params = {
        'about' : home_item
    }
    return render(request, 'home.html', params)

def project(request):
    projects = Project.objects.filter(preview=True)
    params = {
        'projects' : projects,
    }
    return render(request, 'projects.html', params)

def links(request):
    home_item = Home.objects.filter(preview=True)
    all_links = Link.objects.filter(show=True)
    params = {
        'about' : home_item,
        'links' : all_links,
    }
    print(home_item,all_links,params)
    return render(request, 'links.html', params)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        phone = request.POST.get('phone','')
        email = request.POST.get('email','')
        message = request.POST.get('name','')
        print(name, phone, email, message)
    return render(request, 'contact.html')