from rest_framework import serializers
from .models import *

class AnimeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeImage 
        fields = ('id', 'name', 'image', 'generated_image', 'timestamp')


class NotesAnimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = NotesAnime
        fields = '__all__'

