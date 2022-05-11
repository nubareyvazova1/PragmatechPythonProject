from django.urls import path
from blogs.views import blogs, blog_detail

urlpatterns = [
    
    path('<int:pk>', blog_detail),
    
]