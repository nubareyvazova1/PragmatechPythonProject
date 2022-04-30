

from django.urls import path
from accounts.views import users_viwer
urlpatterns = [
    path('',users_viwer),
]
