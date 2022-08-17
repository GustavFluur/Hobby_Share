from django.shortcuts import render, HttpResponse
from Share_Hobby.views import say_hello

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello!")
