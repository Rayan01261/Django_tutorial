from django.shortcuts import render
from django.http import HttpResponse

def index(requet):
    return HttpResponse("Hello, World. You're at the polls index.")
# Create your views here.
