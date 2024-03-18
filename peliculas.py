import requests
import json
import pprint
from omdbapi.movie_search import GetMovie
from 

pelicula = input('hola! que pelicula quieres buscar: ')
movie = f"http://www.omdbapi.com/?&apikey=2e7885f6"

movie = GetMovie(api_key='2e7885f6')
movie.get_movie(title=pelicula)
pprint.pprint(movie.get_data('director'))
