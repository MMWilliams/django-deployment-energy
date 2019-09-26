from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')
#settings knows about this directory because it was added to DIR []
#first_project/first_project
def help(request):
    return render(request, 'help.html')
#first_project/first_app/
def images(request):
    return render(request, 'images.html')

def contactus(request):
    return render(request, 'contactus.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def articles(request):
    return render(request, 'articles.html')

def consulting(request):
    return render(request, 'consulting.html')

def energycosts(request):
    return render(request, 'energycosts.html')

def energyderegulation(request):
    return render(request, 'energyderegulation.html')

def savetoday(request):
    return render(request, 'savetoday.html')

def energyderegulation(request):
    return render(request, 'energyderegulation.html')
