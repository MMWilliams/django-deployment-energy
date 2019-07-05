from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me': 'Hello I am from first_app/index.html'}
    return render(request, 'first_app/index.html',context=my_dict)
#settings nows about this directory because it was added to DIR []

def help(request):
    help_dict = {'help_insert': 'Hello I am from first_app/help.html'}
    return render(request, 'first_app/help.html',context=help_dict)

def images(request):
    images_insert = {'images_insert': 'Hello I am from Statis/images.html'}
    return render(request, 'first_app/images.html',context=images_insert)

def contactus(request):
    contactus_insert = {'contactus_insert': 'Hello I am from Statis/images.html'}
    return render(request, 'first_app/contactus.html',context=contactus_insert)

def aboutus(request):
    aboutus_insert = {'aboutus_insert': 'Hello I am from Statis/aboutus.html'}
    return render(request, 'first_app/aboutus.html',context=aboutus_insert)

def articles(request):
    articles_insert = {'articles_insert': 'Hello I am from Statis/articles.html'}
    return render(request, 'first_app/articles.html',context=articles_insert)

def consulting(request):
    consulting_insert = {'consulting_insert': 'Hello I am from Statis/consulting.html'}
    return render(request, 'first_app/consulting.html',context=consulting_insert)

def energycosts(request):
    energycosts_insert = {'energycosts_insert': 'Hello I am from Statis/energycosts.html'}
    return render(request, 'first_app/energycosts.html',context=energycosts_insert)

def energyderegulation(request):
    energyderegulation_insert = {'energyderegulation_insert': 'Hello I am from Statis/energyderegulation.html'}
    return render(request, 'first_app/energyderegulation.html',context=energyderegulation_insert)

def savetoday(request):
    savetoday_insert = {'savetoday_insert': 'Hello I am from Statis/savetoday.html'}
    return render(request, 'first_app/savetoday.html',context=savetoday_insert)

def energyderegulation(request):
    energyderegulation_insert = {'images_insert': 'Hello I am from Statis/energyderegulation.html'}
    return render(request, 'first_app/energyderegulation.html',context=energyderegulation_insert)
