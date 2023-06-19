import json
import csv
def getCSV(recs):
    f1 = open("data/titles.json", "r")
    data = json.load(f1)
    f1.close()

    f2 = open('rated.csv', 'w')
    # create the csv writer
    writer = csv.writer(f2)


    csvRecs = []
    header = ['item','title','genres','ratings']

    writer.writerow(header)
    
    for title in recs:
        rating = recs[title]
        id = data[title][0]
        genres = data[title][1]

        writer.writerow([id,title,genres,rating])

    f2.close()


# getCSV(['Toy Story (1995), 1', 'Jumanji (1995), 2', "Waiting to Exhale (1995), 5"])

