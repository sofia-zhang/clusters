import csv

f1 = open("data/movies.csv", "r")
lines = f1.readlines()
f1.close()

f2 = open('data/moviesEdited.csv', 'w')
# create the csv writer
writer = csv.writer(f2)
# lines = ['movieId,title,genres','1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy','2,Jumanji (1995),Adventure|Children|Fantasy','3,Grumpier Old Men (1995),Comedy|Romance','4,Waiting to Exhale (1995),Comedy|Drama|Romance']

# print(lines)

dict = {}

for i in range(1, len(lines)):
    if ")," not in lines[i] and ')\",' not in lines[i]:
        for j in range(len(lines[i])-1,0,-1):
            if lines[i][j] == ",":
                lines[i] = lines[i][:j] + "()" + lines[i][j:]
                break

   
    firstComma = lines[i].index(",")
    lastComma = lines[i].rindex(",")

    id = lines[i][:firstComma]
    title = lines[i][firstComma + 1:lastComma]
    genre = lines[i][lastComma + 1:len(lines[i]) - 1]

    writer.writerow([id,title,genre])

f2.close()