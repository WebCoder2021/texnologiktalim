from django.urls import path
from .views import *
urlpatterns = [
    path('login', log_in, name='login'),
    path('check_user', check_user, name='check_user'),
    
]