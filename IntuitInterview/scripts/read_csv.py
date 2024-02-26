import csv
from api.models import Player

def run():
    with open('api/Player.csv') as csvfile:
        reader = csv.reader(csvfile)
        # skip headers
        next(reader)
        # delete all previously filled object
        Player.objects.all().delete()
        # Assign the model to the player
        i = 0
        for row in reader:
            #print(row)
            #print ("#"*20)
            print (i)
            i += 1
            #p = Player(playerId=row[0])

            p = Player(
                playerId=row[0],
                playerBirthYear=row[1],
                playerBirthMonth=row[2],
                playerBirthDay=row[3],
                birthCountry=row[4],
                birthState=row[5],
                birthCity=row[6],
                playerDeathYear=row[7],
                playerDeathMonth=row[8],
                playerDeathDay=row[9],
                deathCountry=row[10],
                deathState=row[11],
                deathCity=row[12],
                nameFirst=row[13],
                nameLast=row[14],
                nameGiven=row[15],
                weight=row[16],
                height=row[17],
                bats=row[18],
                throws=row[19],
                debut=row[20],
                finalGame=row[21],
                retroID=row[22],
                bbrefID=row[23]
            )
            p.save()