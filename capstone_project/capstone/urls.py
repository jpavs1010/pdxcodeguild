from django.conf.urls import url
from . import views

app_name = 'capstone'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getdata/', views.getdata, name='getdata'),
    url(r'^diabetesmap/', views.diabetesmap, name='diabetesmap'),
    url(r'^obesemap/', views.obesemap, name='obesemap')
]
