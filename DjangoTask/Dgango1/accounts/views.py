from django.shortcuts import render
from django.http import HttpResponse

def user_view(request):
    return HttpResponse('My User')
