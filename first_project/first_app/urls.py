from django.conf.urls import url
from first_app import views
from django.conf.urls import include
from . import views


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url('contactus/', views.contactus,name='contactus'),
    url('aboutus/', views.aboutus,name='aboutus'),
    url('images/', views.images,name='images'),
    url('articles/', views.articles,name='articles'),
    url('savetoday/', views.savetoday,name='savetoday'),
    url('energyderegulation/', views.energyderegulation),
    url('consulting/', views.consulting,name='consulting'),

    #url(r'^first_app/',include('first_app.urls')),
    #this needs to be in the directory file
    #url(r'^$',views.index,name='index'),
    #index is housed in views.py
    #url('energycosts/$',views.energycosts,name='energycosts'),#returns index from urls.py in directory




]
