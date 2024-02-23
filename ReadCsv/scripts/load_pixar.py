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
            The next step is to loop over all rows in the CSV. And in this part of the code we find the important method .get_or_create() for the first time. It returns a tuple, where the object at the first index is the Django model object that was created (if it didn’t exist in the database yet) or retrieved (if it already existed). The second element in the tuple is a boolean that returns True if the object was created and False otherwise.

            Notice how we create (or get) the Genre object first, and then use it, together with other information taken from every CSV row, to create a new Film object and save it to the database.
            '''
            genre, _ = Genere.objects.get_or_create(name=row[-1])
            film = Film(title=row[0],
                        year=row[1],
                        genre=genre)
            film.save()
