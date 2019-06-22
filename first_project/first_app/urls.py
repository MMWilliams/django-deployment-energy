from django.conf.urls import url
from first_app import views
from django.conf.urls import include


urlpatterns = [
    url(r'^$',views.index,name='index'),
    #url(r'^first_app/',include('first_app.urls')),
    #this needs to be in the directory file
    #url(r'^$',views.index,name='index'),
    #index is housed in views.py
    url(r'^$',views.help,name='help'),
    url(r'^$',views.images,name='images'),

]
