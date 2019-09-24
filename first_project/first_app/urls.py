from django.conf.urls import url
from first_app import views
from django.conf.urls import include
from . import views


urlpatterns = [

    url(r'^$',views.index,name='index'),
    url(r'contactus/', views.contactus,name='contactus'),
    url(r'aboutus/', views.aboutus,name='aboutus'),
    url(r'images/', views.images,name='images'),
    url(r'articles/', views.articles,name='articles'),
    url(r'savetoday/', views.savetoday,name='savetoday'),
    url(r'energyderegulation/', views.energyderegulation),
    url(r'consulting/', views.consulting,name='consulting'),
    url(r'energycosts/', views.energycosts,name='energycosts'),


    #url(r'^first_app/',include('first_app.urls')),
    #this needs to be in the directory file
    #url(r'^$',views.index,name='index'),
    #index is housed in views.py
    #url('energycosts/$',views.energycosts,name='energycosts'),#returns index from urls.py in directory




]
