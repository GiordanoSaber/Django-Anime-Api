from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AnimeImage
from .serializers import AnimeImageSerializer

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
