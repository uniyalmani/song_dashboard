from django.urls import path
from .views import *


urlpatterns = [
    path('upload_song', UploadSongs.as_view(), name='upload-songs'),
    path('songs', Songs.as_view(), name='songs'),
    path('home', home, name='home'),
    path('profile', profile, name='profile'),
]