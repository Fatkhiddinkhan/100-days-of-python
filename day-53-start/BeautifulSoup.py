from bs4 import BeautifulSoup
import requests

LINK = "https://appbrewery.github.io/Zillow-Clone/"

class ZillowScraper:
    """A class to scrape property links from a Zillow-like website."""
    def __init__(self, url=None):
        """
        Initialize the scraper with a target URL.
        """
        self.url = LINK

        self.html_content = None
        self.soup = None
        self.prop_links = []
        self.prop_prices = []
        self.prop_addresses = []

    def fetch_html(self):
        """
        Fetch the HTML content of the given URL.
        """
        header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        }
        try:
            response = requests.get(self.url, headers=header)
            response.raise_for_status()
            self.html_content = response.text
            print("HTML content fetched successfully.")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the webpage: {e}")
    def parse_html(self):
        """
        Parse the HTML content using Beautiful Soup.
        """
        if self.html_content:
            self.soup = BeautifulSoup(self.html_content, "html.parser")
            print("HTML content parsed successfully.")
        else:
            print("No HTML content to parse. Please fetch the HTML first.")
    def extract_property_links(self):
        """
        Extract property links from the parsed HTML using a specific class name.
        """
        if self.soup:
            elements = self.soup.find_all(class_='property-card-link')
            self.prop_links = [
                element["href"] for element in elements if "href" in element.attrs
            ]
            print(f"Extracted {len(self.prop_links)} property links.")
        else:
            print("Soup object is not initialized. Please parse the HTML first.")
    def extract_property_prices(self):
        """
        Extract property price from the parsed HTML using a specific class name.
        """
        if self.soup:
            elements = self.soup.select(".PropertyCardWrapper__StyledPriceLine")
            self.prop_prices = [
                element.text.split('+')[0].replace("/mo", '') for element in elements
            ]
            print(f"Extracted {len(self.prop_prices)} property links.")
        else:
            print("Soup object is not initialized. Please parse the HTML first")

    def extract_prop_addresses(self):
        """
        Extract property addresses from the parsed HTML using a specific class name.
        """
        if self.soup:
            elements = self.soup.find_all("address")
            self.prop_addresses = [
                element.text.strip() for element in elements
            ]
            print(f"Extracted {len(self.prop_addresses)} property addresses.")
        else:
            print("Soup object is not initialized. Please parse the HTML first")
    def run_scraper(self):
        """
        Run the entire scraper process: fetch, parse, and extract links.
        """
        self.fetch_html()
        self.parse_html()
        self.extract_property_links()
        self.extract_property_prices()
        self.extract_prop_addresses()
    def provide_data(self):
        print("Sending data...")
        return self.prop_addresses, self.prop_prices, self.prop_links