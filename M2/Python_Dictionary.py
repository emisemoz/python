movie= {
    'title': 'Jumanji : The Next Level',
    'year' : 2017,
    'genre' : 'Adventure',
}
movie_2 = {
    'title' : 'Frozen II',
    'year' : 2019,
    'genre' : 'Family',
}
movie.update({'viewers' : 44324578}) #Added new item
movie["genre"]= "Adventure/Comedy" #Changing the genre
del movie ['year'] #Removing year
print(movie)

movie_2.update({'viewers' : 98698637})
movie_2["genre"]="Family/Musical"
print(movie_2)