"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from first_app import views #from this first app, import the views.py
from django.conf.urls import include


#this will return the string within the index called 'index'
#all URLs are housed here
#mapping a view to a urls
#via urls.py and views.py
#using regular expressions

#for each URL, input corresponding object in views.py
urlpatterns = [ #FOR EACH VIEW, INPUT CORRESPONDING VIEWS JOB IN VIEWS.PY
    url(r'^$',views.index,name='index'),
    url(r'^/',views.index,name='index'),#returns index from urls.py in directory
    


    #path('/energycosts',views.energycosts),
    #url(r'^energycosts/,views.index,name='energycosts'),#returns index from urls.py in directory
    #path('energycosts/', views.energycosts),

    url('energycosts/',views.energycosts),#returns index from urls.py in directory
    #path(r'^energycosts/',views.energycosts,name='energycosts'),#returns index from urls.py in directory
    url('contactus/', views.contactus,name='contactus'),
    url('aboutus/', views.aboutus,name='aboutus'),
    url('images/', views.images,name='images'),
    url('articles/', views.articles,name='articles'),
    url('savetoday/', views.savetoday,name='savetoday'),
    url('energyderegulation/', views.energyderegulation,name='energyderegulation'),
    url('consulting/', views.consulting,name='consulting'),
    path('admin/', admin.site.urls),
    url(r'first_app/',include('first_app.urls'))

]
