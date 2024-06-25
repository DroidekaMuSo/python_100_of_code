import requests
from bs4 import BeautifulSoup

response = requests.get(
    url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_archive = response.text

soup = BeautifulSoup(web_archive, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movies_titles = [movie.getText() for movie in all_movies]
movies = movies_titles[::-1]

with open("movies.txt", mode="w") as txt_file:
    for movie in movies:
        txt_file.write(f"{movie}\n")
