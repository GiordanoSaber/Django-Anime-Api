from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class AnimeImageView(APIView):
    def get(self, request):
        anime_images = AnimeImage.objects.all()
        serializer = AnimeImageSerializer(anime_images, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnimeImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class NotesAnimeView(APIView):
    def get(self, request):
        notes_anime = NotesAnime.objects.all()
        serNote = NotesAnimeSerializer(notes_anime, many= True)
        return Response(serNote.data)
    
    def post(self, request):
        serNote = NotesAnimeSerializer(data=request.data)
        if serNote.is_valid():
            serNote.save()
            return Response(serNote.data, status=status.HTTP_201_CREATED)
        return Response(serNote.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, animeNotes_id):
        notes_anime = NotesAnime.objects.get(pk=animeNotes_id)
        serNote = NotesAnimeSerializer(notes_anime, data= request.data)
        if serNote.is_valid():
            serNote.save()
            return Response(serNote.data)
        return Response(serNote.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, animeNotes_id):
        notes_anime = NotesAnime.objects.get(pk=animeNotes_id)
        notes_anime.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    



