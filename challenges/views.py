from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request):
    return HttpResponse("This works!") # response being sent back to client

def february(request):
    return HttpResponse("The beautiful month of February. . .")