from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.showItem,name ='Show_tag')
   
]
