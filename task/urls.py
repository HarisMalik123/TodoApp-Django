
from django.contrib import admin
from django.urls import path
from task import views
urlpatterns = [
    path('',views.todolist,name="todolist"),
    path('add/',views.add_task,name='add_task'),
    
    path('admin/',admin.site.urls)
    

]
