from django.conf.urls import url
from . import views

app_name = 'capstone'
urlpatterns = [
    url(r'^$', views.index2, name='index'),
    url(r'^getdata/', views.getdata, name='getdata'),
    url(r'^getmetadata/', views.getmetadata, name='getmetadata'),
    url(r'^correlation/', views.correlation, name='correlation'),
    url(r'^scatterplot/', views.scatterplot, name='scatterplot')
]
