from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=url)
web_page = response.text


soup = BeautifulSoup(web_page, "html.parser")
movies_name = soup.find_all(name="h3", class_="title")
for movie in movies_name[100:: -1]:
    with open(file="films.txt", mode="a") as file:
        file.write(movie.getText() + "\n")
