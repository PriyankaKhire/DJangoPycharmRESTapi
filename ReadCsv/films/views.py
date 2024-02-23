from django.shortcuts import render
from django.http import HttpResponse

from films.models import Film
from films.serializers import FilmSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
def home(request):
    return HttpResponse('This is the home page')

class FilmList(APIView):
    def get(self, request):
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)