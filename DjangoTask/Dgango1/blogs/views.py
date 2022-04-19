from django.shortcuts import render
context={'title':'My Blogs1'}

def blogs (request):
    return render(request ,"blogs/my_blog.html" ,context=context)
    
  
