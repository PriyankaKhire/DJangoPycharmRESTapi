# Creating REST api to read CSV and get its contents

## Install Poetry for dependency and django extensions
```angular2html
pip install poetry
poetry init
poetry add Django djangorestframework
pip install django django-extensions pandas plotly
```
## Update the settings.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add the extensions
    'rest_framework', 
    'django_extensions'
]
```
## Test the server
```angular2html
python manage.py runserver
```
## Check the errors
```angular2html
python manage.py check
```
## Add web app to the server
```angular2html
python manage.py startapp <webapp_name>
```
## Add this webapp to settings.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add the extensions
    'rest_framework',
    'django_extensions', # don't forget comma
    # add the webapp
    'mywebapp.apps.MywebappConfig'
]
```
## Change home page view
- Under mywebapp/views.py add
```python
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return HttpResponse("This is my homepage")
```
- Update the urls.py
```python
from mywebapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage')
]
```

## Add MyWebapp under paths
- Let's first create the view for it
- Under mywebapp/views.py add
```python
from rest_framework.views import APIView
from django.http import HttpResponse

class MyWebAppView(APIView):
    # GET call
    def get(self, request):
        return HttpResponse("This is get function")
```
- Under mywebapp folder create urls.py
- Populate it with following to add the GET view:
```python
from django.urls import path

from mywebapp import views

urlpatterns = [
    path('', views.MyWebAppView.as_view())
]
```
- Add this url path under main urls.py
```python
from django.contrib import admin
from django.urls import path, include
from mywebapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('mywebapp/', include('mywebapp.urls'))
]
```
## Check the server
- Run the server
```angular2html
python manage.py runserver
```
- Then go to http://127.0.0.1:8000/mywebapp/

## Read the CSV
- Create the csv under mywebapp folder
- Add Migrations
```angular2html
python manage.py migrate
```
- Update the mywebapp/models.py
```python
from django.db import models

# Create your models here.
class Alphabets(models.Model):
    id = models.IntegerField(primary_key=True) # Making id as Primary Key
    name = models.CharField(max_length=10)
```
- Make migrations
```angular2html
python manage.py makemigrations
python manage.py migrate
```
### Create the Script to read CSV
- Create folder **scripts** <- This needs to be the EXACT spelling of the folder
- Inside this folder create a python file, name it what ever, I am calling it read_csv_file
- This file won't run if it does not have run function in it.
- Populate the file with this code
```python
import csv
from mywebapp.models import Alphabets

def run():
    with open('mywebapp/mycsvfile.csv') as file:
        reader = csv.reader(file)
        # skip the csv file headers
        next(reader)
        # Clear the previously imported models
        Alphabets.objects.all().delete()
        for row in reader:
            print(row)
            alphabet = Alphabets(id=row[0], name=row[1])
            alphabet.save()
```
- To run this file we type
```angular2html
(.venv) PS C:\Users\priya\Documents\GitHub\DJangoPycharmRESTapi\ReadCsvAndGET> python .\manage.py runscript read_csv_file
```
- This will import all data into the models

## View the contents of Data Model
- Create mywebapp/serializer.py 
```python
from rest_framework import serializers

from mywebapp.models import Alphabets


class AlphabetSerializer(serializers.ModelSerializer):
    class Meta:
        # Import the Data model to serialize
        model = Alphabets
        fields = '__all__'
```
- Update the get function under views.py
```python
from django.http import HttpResponse
from rest_framework.response import Response # This is the response for the get
from rest_framework.views import APIView

from mywebapp.models import Alphabets
from mywebapp.serializer import AlphabetSerializer


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
```
## Get All Names
- Create Serilizer 
```python
from rest_framework import serializers

from mywebapp.models import Alphabets

# This displays all fields
class AlphabetSerializer(serializers.ModelSerializer):
    class Meta:
        # Import the Data model to serialize
        model = Alphabets
        fields = '__all__'

# This only displays name field
class AlphabetNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alphabets
        fields = ['name']
```
- Create the view for this new GET request
- Notice there is no difference between two classes
- The only difference is the serializer
```python
from django.http import HttpResponse
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
```
- Tie the view to urls
```python
from django.urls import path

from mywebapp import views

urlpatterns = [
    path('', views.MyWebAppView.as_view()), # Don't forget the comma
    path('getAllAlphabets', views.GetAllNamesView.as_view())
]
```
### To test visit
- http://127.0.0.1:8000/mywebapp/getAllAlphabets

## Get Name by ID
- Create the view
```python
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView

from mywebapp.models import Alphabets


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
```
- Tie the view to urls
```python
from django.urls import path

from mywebapp import views

urlpatterns = [
    path('', views.MyWebAppView.as_view()), # Don't forget the comma
    path('getAllAlphabets', views.GetAllNamesView.as_view()),
    path('getNameById', views.GetAlphabetByIdView.as_view())
]
```
- Test the api by going to:
  - http://127.0.0.1:8000/mywebapp/getNameById # Error Case
  - http://127.0.0.1:8000/mywebapp/getNameById?id=5
  - http://127.0.0.1:8000/mywebapp/getNameById?id=55 # Error Case

# Testing the Project
- Go to mywebapp/tests.py and setup basic testing framework
```python
from django.test import TestCase

# Create your tests here.
class TestCsvAndGET(TestCase):

    def setUp(self):
        print("setUp: Setting up clean data")
        pass

    def tearDown(self):
        print("tearDown: Tearing down the data")
        pass

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Setting up test data for all class methods")
        pass

    def test_firstTest(self):
        print("test_firstTest: This is the first test here")
        self.assertEqual(True, True)
```
- The file will run anything that starts with test
- To run the test just click on the play button
- You can see the following in the output 
```angular2html
setUpTestData: Setting up test data for all class methods
setUp: Setting up clean data
test_firstTest: This is the first test here
tearDown: Tearing down the data
```
- These are all the print statements given by you

## Testing Data Model
```python
from django.test import TestCase

from mywebapp.models import Alphabets

class TestDataModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create some fake data
        Alphabets.objects.create(id=1, name="Alphabet")

    def test_id(self):
        alphabet = Alphabets.objects.get(id=1)
        self.assertEqual(alphabet.id, 1)

    def test_name(self):
        alphabet = Alphabets.objects.get(id=1)
        self.assertEqual(alphabet.name, "Alphabet")
```
## Testing Views
```python
from django.test import TestCase
from django.urls import reverse

from mywebapp.models import Alphabets

class TestViews(TestCase):
    @classmethod
    def setUpTest(cls):
        Alphabets.objects.create(id=1, name="Alphabet1")
        Alphabets.objects.create(id=2, name="Alphabet2")
        Alphabets.objects.create(id=3, name="Alphabet3")

    def test_get_myWebAppView(self):
        response = self.client.get('/mywebapp/')
        self.assertEqual(response.status_code, 200)

    def test_get_getAllNamesView(self):
        response = self.client.get('/mywebapp/getAllAlphabets')
        self.assertEqual(response.status_code, 200)

    def test_get_getAlphabetByIdView(self):
        response = self.client.get('/mywebapp/getNameById')
        self.assertEqual(response.status_code, 400)
```