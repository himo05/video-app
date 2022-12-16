from django.urls import path 
from . import views 

# URL patterns for the video app
urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    # Page for adding a new video
    path('add', views.add, name='add_video'),
    # Page for listing all videos
    path('video_list', views.video_list, name='video_list')
]

