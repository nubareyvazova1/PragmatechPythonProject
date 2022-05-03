from django.urls import path
from blogs.views import blogs, blog_detail

urlpatterns = [
    path('', blogs),
    path('<int:pk>', blog_detail),
    
]