from django.conf.urls import url
from first_app import views
from django.conf.urls import include
from . import views


urlpatterns = [ #FOR EACH VIEW, INPUT CORRESPONDING VIEWS JOB IN VIEWS.PY
    url(r'^$',views.index,name='index'),
    url(r'^/',views.index,name='index'),#returns index from urls.py in directory
    url('energycosts/', views.energycosts,name='energycosts'),
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
