from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def function(request):
    return HttpResponse("Yo This Backend is Running")