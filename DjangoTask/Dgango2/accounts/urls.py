

from django.urls import path
from accounts.views import user_view, register
urlpatterns = [
    path('',user_view),
    path('register/',register),
]
