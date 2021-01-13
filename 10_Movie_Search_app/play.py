import requests
import collections

MovieResult = collections.namedtuple(
        'MovieResult',
        "imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres"
        )

search = input("What movie do you want to search for? ")
url = 'https://movieservice.talkpython.fm/api/search/{}'.format(search)

resp = requests.get(url)
resp.raise_for_status()


movie_data = resp.json()
movies_list = movie_data.get('hits')



#for md in movies_list:
#    m = MovieResult(
#            imdb_code=md.get('imdb_code'),
#            title=md.get('title'),
#            duration=md.get('duration'),
#            director=md.get('director'),
#            year=md.get('year',0),
#            rating=md.get('raiting',0),
#            imdb_score=md.get('imdb_score', 0.0),
#            keywords=md.get('keywords'),
#            genres=md.get('genres')
#            )
#    movies.append(m)

movies = [
        MovieResult(**md)
        for md in movies_list
        ]


print("Found {} movies for search {}".format(len(movies), search))
for m in movies:
    print("{} -- {}".format(m.year, m.title))



