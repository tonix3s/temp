from django.conf.urls import url
from django.urls import path
from notes import views

urlpatterns = [

#views.index refére a la function index dans views.py
path('',views.index,name='index'),

#url(r'^$',views.index,name='index'),
]
