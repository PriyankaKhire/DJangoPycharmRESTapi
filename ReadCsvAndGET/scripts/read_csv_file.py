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
