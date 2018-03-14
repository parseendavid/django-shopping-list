from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def login(request):
    return HttpResponse("Welcome to login page")

def register(request):
    return HttpResponse("Welcome to login page")
