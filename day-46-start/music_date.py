from bs4 import BeautifulSoup
import requests

billboard_url = "https://www.billboard.com/charts/hot-100/"
billboard_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

class MusicData:
    def __init__(self, date):
        self.date = date
        self.billboard_response = None
        self.songs = None
        self.request()
    def request(self):
        try:
            response = requests.get(url=f"{billboard_url}{self.date}/", headers=billboard_header)
            if response.status_code == 200:
                self.billboard_response = response
                print(f"Success! Status code: {response.status_code}")
                self.songs = self.fetch_data()
            else:
                print(f"Invalid date or response. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")
            self.billboard_response = None
    def fetch_data(self):
        web_page = self.billboard_response.text
        soup = BeautifulSoup(web_page, "html.parser")
        song_names = soup.select("li ul li h3")
        return [song.getText().strip() for song in song_names]
