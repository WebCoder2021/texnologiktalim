from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('library', library, name='library'),
    path('resurs', resurs, name='resurs'),
    path('video_lesson', video_lesson, name='video_lesson'),
    
]