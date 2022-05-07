from django.shortcuts import render

# Create your views here.



def blogs(request):
    
    return render (request ,'myblogs.html')

def blog_detail(request,pk):
    blogs=[
        {
            1:{
                'author':'Sevinc',
                'title':'Python',
                'publish_data':'12.4.2002',
            },
            2:{
                'author':'Gulnur',
                'title':'Django',
                'publish_data':'15.6.2002',
            },
            
        }
    ]
    blog = blogs[0][pk]
   print(<src>)
    return render (request, 'blog_detail.html', {'blog': blog})