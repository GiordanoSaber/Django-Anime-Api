from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('anime-images/', AnimeImageView.as_view()),
    path('anime_notes/', NotesAnimeView.as_view()),
   
]