from rest_framework import serializers
from .models import AnimeImage

class AnimeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeImage 
        fields = ('id', 'name', 'image', 'generated_image', 'timestamp')
