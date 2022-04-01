from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def blogs(request):
    print(request)
    return HttpResponse('my first app')