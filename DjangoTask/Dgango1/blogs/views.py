from django.shortcuts import render
context={'title':'My Blogs1'}

def blogs (request):
    return render(request,"blogs/my_blogs.html" ,context=context)
    
  
