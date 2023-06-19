import json

f1 = open("data/moviesEdited.csv", "r")
lines = f1.readlines()
f1.close()


# lines = ['movieId,title,genres','1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy','2,Jumanji (1995),Adventure|Children|Fantasy','3,Grumpier Old Men (1995),Comedy|Romance','4,Waiting to Exhale (1995),Comedy|Drama|Romance']

# print(lines)

dict = {}

for i in range(1, len(lines)):
    # print(lines[i])
    # print(lines[i].count(")"))

    data = []
    split = 0
    

    if ")" in lines[i]:
        if ")\"" in lines[i]:
            data = lines[i].strip().split(")\"")
            genre = data[1][1:len(data[1])]

            split = data[0].index(",")

            title = data[0][split + 2:len(data[0])] + ")"

        elif lines[i].count(")") > 1:

            
            data = lines[i].strip().split("),")
            # print(lines[i])
            genre = data[1][:len(data[1])]

            split = data[0].index(",")

            title = data[0][split + 1:len(data[0])] + ")"

        else:
            data = lines[i].strip().split(")")
            print(data)
            
            genre = data[1].split(",")[1]

            split = data[0].index(",")

            title = data[0][split + 1:len(data[0])] + ")"
            title.replace("\"", "")


        
        id = data[0][0:split]
        dict[title] = [id,genre]
    
    # print(title, id, genre)

    
   
# print(dict)



#Save the json object to a file
f2 = open("data/titles.json", "w")
json.dump(dict, f2, indent = 4)
f2.close()
