from django.urls import path
from blogs.views import blogs
urlpatterns = [
    path('',blogs),
    
]