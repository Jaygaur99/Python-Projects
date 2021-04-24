import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/list/ls043593410/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')
all_movies = soup.findAll(name="h3", class_="lister-item-header")
movie_titles = [item.a.getText() for item in all_movies]
# print(movie_titles)
with open('movies.txt', 'w') as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")