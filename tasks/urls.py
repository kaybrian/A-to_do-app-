from django.conf.urls import url,include
from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('',views.index,name='index'),
    path('update/<str:pk>/',views.updateTask,name='update_task'),
    path('delete/<str:pk>/',views.deleteTask,name='delete_task'),
]
