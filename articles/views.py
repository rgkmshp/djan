from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    response = HttpResponse("Hello, its my first site!")
    return response