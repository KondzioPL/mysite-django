from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index, name='index'),
    path('test',views.test, name='test'),
    path('',views.startpage,name ='login')
]
