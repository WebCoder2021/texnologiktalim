from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def module(request):
    return HttpResponse('Hello module')