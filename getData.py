def getData(dict):
    totalWatched = 0
    totalRating = 0

    for key in dict:
        # print(dict[key])
        if dict[key][0] == 'on':
            totalWatched += 1
            totalRating += float(dict[key][1])

    avgWatched = totalWatched / 10
    avgRating = totalRating / totalWatched
    return [avgWatched, avgRating]