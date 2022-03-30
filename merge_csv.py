import csv 

with open ("flask1/movies.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]


headers.append("poster_link")

with open ("flask1/final.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow(headers)

with open ("flask1/movie_links.csv") as t:
    reader = csv.reader(t)
    data = list(reader)
    all_links = data[1:]


for item in all_movies:
    poster = any(item[8] in movie_link_item for movie_link_item in all_links)
    if poster == True:
        for movie_link_item in all_links:
            if item[8] == movie_link_item[0]:
                item.append(movie_link_item[1])
                if len(item) == 28:
                    with open("flask1/final.csv", "a+") as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(item)

