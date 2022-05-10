from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def blogs(request):
    return HttpResponse('my django app')

def accounts(request):
    return render(request,'base.html')