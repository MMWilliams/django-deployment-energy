from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'first_app/index.html')
#settings knows about this directory because it was added to DIR []

def help(request):
    return render(request, 'first_project/first_app/help.html')

def images(request):
    return render(request, 'first_app/images.html')

def contactus(request):
    return render(request, 'first_project/first_app/contactus.html')

def aboutus(request):
    return render(request, 'first_project/first_app/aboutus.html')

def articles(request):
    return render(request, 'first_project/first_app/articles.html')

def consulting(request):
    return render(request, 'first_project/first_app/consulting.html')

def energycosts(request):
    return render(request, 'first_project/first_app/energycosts.html')

def energyderegulation(request):
    return render(request, 'first_app/energyderegulation.html')

def savetoday(request):
    return render(request, 'first_project/first_app/savetoday.html')
