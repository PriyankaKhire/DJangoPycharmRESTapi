from django.shortcuts import render
from django.http import HttpResponse

from films.models import Film
from films.models import UserInfo
from films.serializers import FilmSerializer, UserInfoSerializer
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

class UserInfoListView(APIView):
    def get(self, request):
        print("#"*50)
        print(request.GET.get('name'))
        return HttpResponse(request.GET.get('name'))
