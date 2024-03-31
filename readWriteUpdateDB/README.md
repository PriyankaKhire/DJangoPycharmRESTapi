# Connect MySQL DB to Django and Create REST api to read, display and update its contents

## Install Poetry for dependency and django extensions
```yaml
# Installs Poetry dependency manager
pip install poetry
# Will create pyproject.toml config file where you can specify all dependencies.
poetry init 
# Adds Django framework inside pyproject.toml
poetry add Django djangorestframework
# Installs pytz, tenacity, six, numpy, python-dateutil, plotly, django-extensions, pandas
pip install django django-extensions pandas plotly
```

## Update the settings.py
```yaml
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
```yaml
python manage.py runserver
```
Visit http://127.0.0.1:8000/ to see if it started successfully or not.

## Check the errors
```yaml
python manage.py check
```

## Add web app to the server
```yaml
python manage.py startapp <webapp_name>
```

## Add this webapp to settings.py
```yaml
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
## Add django-mysql
- Go to PyCharm -> Packages (located in bottom left) -> search for django-mysql and install it.
- Go to settings.py
```yaml
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_extensions',
    'webapp.apps.WebappConfig',
    # add the django mysql dependency 
    'django_mysql'
]
```

## Check if we have errors in DB
```yaml
python manage.py check --database default
```

## Install mysqlclient
- Go to PyCharm -> Packages (located in bottom left) -> search for mysqlclient