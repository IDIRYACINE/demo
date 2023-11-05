from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

def data_mine_movies(raw) :
    
    raw = raw.replace('\\', '')

    soup = BeautifulSoup(raw, 'html.parser')
    movies = []
    for movie in soup.select('li.ipc-metadata-list-summary-item'):
        title = movie.select_one('h3.ipc-title__text').text
        descriptions = movie.select('div.cli-title-metadata > span.cli-title-metadata-item')
        year = descriptions[0].text
        duration = descriptions[1].text
        adult_rating = descriptions[2].text if len(descriptions) > 2  else  'N/A'
        ratings = movie.select_one('div.cli-ratings-container > span.ipc-rating-star')

        movies.append({
            'title': title,
            'year': year,
            'duration': duration,
            'adult_rating': adult_rating,
            'rating': ratings.text
        })

    with open('movies.json', 'w') as outfile:
        json.dump(movies, outfile, indent=4)

def scrape_top_250_movies() :
    driver_path = '/home/idir/WebDrivers/chromedriver'
    service = webdriver.ChromeService(executable_path=driver_path)

    driver = webdriver.Chrome(service=service)
    driver.get('https://www.imdb.com/chart/top?ref_=nv_mv_250_6')

    driver.implicitly_wait(10)

    content = driver.find_element(By.CLASS_NAME, 'ipc-metadata-list')

    with open('raw.json', 'w') as outfile:
        json.dump(content.get_attribute('innerHTML'), outfile, indent=4)

    driver.quit()



# scrape_top_250_movies()
data_mine_movies(open('raw.json').read())