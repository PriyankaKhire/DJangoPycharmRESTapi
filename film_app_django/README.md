# REST API using PyCharm Python 3.12 and Django

## Getting started
- Open PyCharm and Select Django Project
- Select Python version
- Create the Project

## Using Poetry as dependency tool
- in the terminal type 

```pip install poetry```

- To initialize poetry type 

```poetry init```

- To get the default settings just press enter for the prompts that follow
- To create a virtual environment type 

```poetry shell```

- Next add django rest framework
  
```poetry add Django djangorestframework```

## Add Migrations

- To add Migrations
  
```python manage.py migrate```

## Add django rest framework 

- Go to settings.py 
- Under INSTALLED_APPS add 'rest_framework'

## To run the server

- Type the following
  
```python manage.py runserver```

- Go to http://127.0.0.1:8000/ to see if the server is running or not

# To add a webapp to our server

- Type the following
  
```python manage.py startapp <webapp name>```

- Add this newly created webapp to settings.py under INSTALLED_APPS 

# Add webapp class to models

- Create your database model under models.py under your webapp
- Then migrate models
  
```python manage.py makemigrations```

- Then type
  
```python manage.py migrate```

# To view the models 

- Create the serializers file under your webapp

```python
from rest_framework import serializers

from film.models import Film


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

``` 

# Create get and post view

- In views.py under your webapp
```python
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


```

# To connect the view and the urls

- Create urls.py file under webapp

```python
from django.urls import path

from film import views
    
    
urlpatterns = [
    path('', views.FilmList.as_view())
]
```

## Connect our webapp urls under django webapp urls

- Under webapp_django to to urls.py 
```python
"""
URL configuration for film_app_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('films/', include('film.urls'))
]

```

## To change the path of the GET API

- Go uder webapp/urls.py

```python
from django.urls import path

from film import views
    
    
urlpatterns = [
    path('v1/viewList', views.FilmList.as_view())
]
```
![Screenshot 2024-02-22 180849](https://github.com/PriyankaKhire/DJangoPycharmRESTapi/assets/12015512/9c13d711-d4f1-42e7-bb24-8c48a49c235c)

