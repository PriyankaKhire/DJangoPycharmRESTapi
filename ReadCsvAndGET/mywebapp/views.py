from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response # This is the response for the get
from rest_framework.views import APIView

from mywebapp.models import Alphabets
from mywebapp.serializer import AlphabetSerializer
from mywebapp.serializer import AlphabetNamesSerializer


# Create your views here.
def homepage(request):
    return HttpResponse("This is my homepage")

class MyWebAppView(APIView):
    # GET call
    def get(self, request):
        # get all the objects
        alphabets = Alphabets.objects.all()
        serializer = AlphabetSerializer(alphabets, many=True)
        return Response(serializer.data)

class GetAllNamesView(APIView):
    # Get call
    def get(self, request):
        # Get all objects
        alphabets = Alphabets.objects.all()
        # Only display names
        nameSerializer = AlphabetNamesSerializer(alphabets, many=True)
        return Response(nameSerializer.data)

class GetAlphabetByIdView(APIView):
    # Get call
    def get(self, request):
        # get the id from the request
        alphabetId = request.GET.get('id')
        try:
            # get name of the player from the id
            alphabetObj = Alphabets.objects.get(id=alphabetId)
        except:
            return HttpResponse("Omg that's wrong", status=status.HTTP_400_BAD_REQUEST)
        else:
            return HttpResponse(alphabetObj.name, status=status.HTTP_200_OK)
