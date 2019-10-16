from django.conf.urls import url
from first_app import views
from django.conf.urls import include
from . import views
from django.urls import path


urlpatterns = [ #FOR EACH VIEW, INPUT CORRESPONDING VIEWS JOB IN VIEWS.PY
    url(r'^',views.index,name='index'),
    url(r'^$',views.index,name='index'),
    #url(r'^/',views.index,name='index'),#returns index from urls.py in directory
    url(r'energycosts/', views.energycosts,name='energycosts'),
    url(r'contactus/', views.contactus,name='contactus'),
    url(r'aboutus/', views.aboutus,name='aboutus'),
    url(r'images/', views.images,name='images'),
    url(r'articles/', views.articles,name='articles'),
    url(r'savetoday/', views.savetoday,name='savetoday'),
    url(r'energyderegulation/', views.energyderegulation,name='energyderegulation'),
    url(r'consulting/', views.consulting,name='consulting'),
    #path(r'^admin/',admin.site.urls),
    url(r'first_app/',include('first_app.urls'))






]
