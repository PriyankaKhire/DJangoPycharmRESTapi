from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from film.models import Film
from film.serializers import FilmSerializer


# Create your views here.
class FilmList(APIView):
    # GET request view
    def get(self, request):
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)

    # POST request view
    def post(self, request):
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # if the request is valid the return success
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if the request is invalid then return error status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

