from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def index(request):
    return render(request, 'first_app/index.html')
    csrf_protect()
#settings nows about this directory because it was added to DIR []

def help(request):
    return render(request, 'first_app/help.html')

def images(request):
    return render(request, 'first_app/images.html')

def contactus(request):
    return render(request, 'first_app/contactus.html')

def connect(request):
    return render(request, 'first_app/connect.php')

def aboutus(request):
    return render(request, 'first_app/aboutus.html')

def articles(request):
    return render(request, 'first_app/articles.html')

def consulting(request):
    return render(request, 'first_app/consulting.html')

def energycosts(request):
    return render(request, 'first_app/energycosts.html')

def energyderegulation(request):
    return render(request, 'first_app/energyderegulation.html')

def savetoday(request):
    return render(request, 'first_app/savetoday.html')

def energyderegulation(request):
    return render(request, 'first_app/energyderegulation.html')
#connected to form
def createpost(request):
        if request.method == 'Submit':
            if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                post.title= request.Submit.get('title')
                post.content= request.Submit.get('content')
                post.save()

                return render(request, 'first_app/index.html')

        else:
                return render(request,'first_app/index.html')

def get(request):
  context = RequestContext(request)
  context_dict = {}
  # Update the dictionary with csrf_token
  conext_dict.update(csrf(request))
  return render_to_response("index.html", context_dict, context)
