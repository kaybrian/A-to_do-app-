from django.conf.urls import url,include
from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('',views.index,name='index'),
]