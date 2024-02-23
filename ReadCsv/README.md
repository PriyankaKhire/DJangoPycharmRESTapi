# REST API using PyCharm Python 3.12 and Django

# Sources
- https://towardsdatascience.com/django-first-steps-for-the-total-beginners-a-quick-tutorial-5f1e5e7e9a8c
- https://towardsdatascience.com/use-python-scripts-to-insert-csv-data-into-django-databases-72eee7c6a433

- [Reading CSV](https://python.plainenglish.io/importing-csv-data-into-django-models-c92a303623fe)

## YouTube tutorial:
[Django - PyCharm #1: Create a Simple REST API with Django](https://www.youtube.com/watch?v=iWPS2HiXUSg&ab_channel=BoilerTech)

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

## Add django rest framework 

- Go to settings.py 
- Under INSTALLED_APPS add 'rest_framework'

## Add django extensions

- Add django_extensions
- Run the following command

```pip install django django-extensions pandas plotly```

- Go to settings.py
- Under INSTALLED_APPS add 'django_extensions'

## To run the server

- Type the following
  
```python manage.py runserver```

- Go to http://127.0.0.1:8000/ to see if the server is running or not

## To add a webapp to our server

- Type the following
  
```python manage.py startapp <webapp name>```

- here webapp name is films

- Add this newly created webapp to settings.py under INSTALLED_APPS 

```'films.apps.FilmsConfig'```

## To change the home page add 

- Go to ReadCsv/urls.py add

```python
urlpatterns = [
    path('', views.home, name='home'), # add this line
    path('admin/', admin.site.urls),
]
```

- Go to films/views.py add

```python
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('This is the home page')
```

## To check code for errors

- Run the following in terminal 

```python manage.py check```


## Crete API path by adding urls.py under films Project

- Create urls.py under films directory
- Add this new route to our main project by adding the following 

```python
from django.contrib import admin
from django.urls import path
from django.urls import include # add this line 
from films import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('films/', include('films.urls')),    # add this line 
]
```

## Creating main and user_info page view 

- Under films/urls.py add this as url pattern

```python
urlpatterns = [
    path('', views.main, name='main'), # here views.main is the function 
    path('user_info/', views.user_info, name='user_info'),
]
```

- Create the view for these 2 pages
- Under films/views.py add the following 2 functions 

```python
def main(request): # this is the implementation of the main function 
    return HttpResponse('This is the main films page')

def user_info(request):
    return HttpResponse('This is the user info page')
```

- To see the view visit 
  - http://localhost:8000/films/
  - http://localhost:8000/films/user_info
  
  
## Add Migrations TO CREATE YOUR OWN DATABASE TABLES

- To add Migrations
  
```python manage.py migrate```

## Add webapp class to models

- Create your database model under models.py under your webapp

```python
from django.db import models

# Create your models here.
class Genere(models.Model):
    name = models.CharField(max_length=150)

    # This returns the string name
    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    # This is a foreign key it's a one-to-many relationship 
    genre = models.ForeignKey(Genere, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

- Then migrate models
  
```python manage.py makemigrations```

- Then type
  
```python manage.py migrate```

# Read the CSV 

- Create the csv under films/pixar.csv 
- See the file in the folders above
- Create ReadCsv/scripts/load_pixar.py

```python
from films.models import Film
from films.models import Genere
import csv

def run():
    with open('films/pixar.csv') as file:
        reader = csv.reader(file)
        next(reader) # to skip the csv file headers

        # Remove any previously populated instances in the model
        Film.objects.all().delete()
        Genere.objects.all().delete()

        for row in reader:
            print(row)

            '''
            The next step is to loop over all rows in the CSV. 
			And in this part of the code we find the important method .get_or_create() for the first time. 
			It returns a tuple, where the object at the first index is the Django model object that was created (if it didn’t exist in the database yet) 
			or retrieved (if it already existed). The second element in the tuple is a boolean that returns True if the object was created and False otherwise.

            Notice how we create (or get) the Genre object first, and then use it, 
			together with other information taken from every CSV row, to create a new Film object and save it to the database.
            '''
            genre, _ = Genere.objects.get_or_create(name=row[-1])
            film = Film(title=row[0],
                        year=row[1],
                        genre=genre)
            film.save()

```

- To run the script type 

```python .\manage.py runscript load_pixar```

- Notice there is not .py at the end of the load_pixar

- Changing the view 
  - Go to films/views.py
  ```python
  class FilmList(APIView):
    def get(self, request):
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)
  ```

- Update the urls
```python
from django.urls import path

from films import views

urlpatterns = [
    path('', views.FilmList.as_view()),
]
```

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
```



