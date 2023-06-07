from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
   
   path('',views.index,name='index'),
   path('<int:id>',views.view_car,name='view_car'),
   path('add/',views.add,name='add'),
]
