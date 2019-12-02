from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def startpage(request):
    return HttpResponse("<p ALIGN=CENTER>MAKE A SPACESHIP</p>")

def index(request):

    return HttpResponse("<p ALIGN=CENTER><font=10>MAKE YOUR OWN SPACESHIP</font></p>")


def test(request):
    return HttpResponse("to jest test")
    p = User(name = 'user1', password = 'qwerty123', email = 'qwerty@gmail.com')
    p.save
    return HttpResponse("to jest test")
    
