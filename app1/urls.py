from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns=[
    path('',views.home,name = 'home'),
    url(r'^predict/$',views.predict,name= 'predict'),
]