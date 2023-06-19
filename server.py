# flask --app data_server run
from flask import Flask
from flask import render_template
from flask import request
from parseMovies import getCSV
from recommender import getRecs, getGeneralRecs
from getData import getData
import csv
import json
import sys
import markupsafe

app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/')
@app.route('/index')
def index():
    f = open("data/titles.json", "r")
    data = json.load(f)
    f.close()
    
    
    if request.method == "GET":
        movies = data.keys()
    
    return render_template('index.html', movies = movies)

@app.route('/recs')
def recs():
    r = {}
    for i in range(1,7):
        title = request.args.get("title" + str(i))
        rating = request.args.get("rat" + str(i))

        r[title] = rating
    

    getCSV(r)
    # print(getRecs())
    recs = {}
    # recs["general"] = getGeneralRecs()
    recs["small"] = getRecs("small")
    recs["regular"] = getRecs("reg")
    recs["large"] = getRecs("large")

    org = {}
    
    for rec in recs.keys():
        if recs[rec].empty == False:
            org[rec] = []
            for ind in recs[rec].index:
                org[rec].append([recs[rec]["title"][ind], recs[rec]["genres"][ind]])


    # print(org)

    return render_template('recs.html', org = org)

@app.route("/thanks", methods=["POST", "GET"])
def end():

    
    f = open('testData.csv', 'a')
    # create the csv writer
    writer = csv.writer(f)


    # print(request.args)
    ratings = {}
    for item in request.args:

        if item[0] not in ratings.keys():
            ratings[item[0]] = {}
        
        num2 = item[1]
        if "10" in item:
            num2 = "10"
        if num2 not in ratings[item[0]]:
            ratings[item[0]][num2] = []

        ratings[item[0]][num2].append(request.args.get(item))
        
    for key in ratings:
        d = getData(ratings[key])
        d.insert(0,key)

        writer.writerow(d)
    
    f.close()
    return render_template("thanks.html")
    
app.run(debug=True)
