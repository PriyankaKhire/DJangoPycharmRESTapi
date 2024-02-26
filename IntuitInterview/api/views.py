from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Player
from api.serializer import IntuitSerializer


# Create your views here.
def homepage(request):
    return HttpResponse("Hello, world. You're at the home page of my app")

class MyAPIView(APIView):
    def get(self, request):
        try:
            # Read the request
            playerId = request.GET.get('playerID')
            pageNumber = request.GET.get('page')
            # if player ID is none then we display all players
            if (playerId == None):
                # Can add pagination but don't have time now
                player = Player.objects.all()
                # Paginate the objects
                paginator = Paginator(player, 10)
                if (pageNumber == None):
                    pageNumber = 1
                page_obj = paginator.get_page(pageNumber)
                serializer = IntuitSerializer(page_obj, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                player = Player.objects.get(playerId=playerId)
                serializer = IntuitSerializer(player)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            # Can display what bad request or send out different http codes in the future
            return HttpResponse(e, status=status.HTTP_400_BAD_REQUEST)