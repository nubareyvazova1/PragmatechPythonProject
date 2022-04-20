from django.shortcuts import render
context={'title': "my work"}

def blogs (request):
    return render(request ,"my_blogs.html" ,context=context)
  
