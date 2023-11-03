import requests
from bs4 import BeautifulSoup
import json

def scrape_top_250_movies():
    url = 'http://www.imdb.com/chart/top?ref_=nv_mv_250_6'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = []
    for movie in soup.select('tbody.lister-list tr'):
        title = movie.select_one('td.titleColumn a').text
        year = movie.select_one('td.titleColumn span.secondaryInfo').text.strip('()')
        rating = movie.select_one('td.ratingColumn strong').text
        cast = [actor.text for actor in movie.select('td.titleColumn a')[1:]]
        genre = movie.select_one('td.titleColumn span.genre').text.strip()
        description_url = 'http://www.imdb.com' + movie.select_one('td.titleColumn a')['href']
        description_response = requests.get(description_url)
        description_soup = BeautifulSoup(description_response.text, 'html.parser')
        description = description_soup.select_one('div.summary_text').text.strip()
        length = description_soup.select_one('div.subtext time').text.strip()
        movies.append({
            'title': title,
            'year': year,
            'rating': rating,
            'cast': cast,
            'genre': genre,
            'description': description,
            'length': length
        })
    with open('movies.json', 'w') as outfile:
        json.dump(movies, outfile, indent=4)
