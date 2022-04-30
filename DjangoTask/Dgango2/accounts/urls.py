

from django.urls import path
from accounts.views import users
urlpatterns = [
    path('',users),
]
