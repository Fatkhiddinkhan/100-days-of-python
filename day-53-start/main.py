from BeautifulSoup import ZillowScraper
from Selenium import GoogleSheetBot

zillow_data = ZillowScraper()
zillow_data.run_scraper()
address, price, link = zillow_data.provide_data()

auto_bot = GoogleSheetBot()
auto_bot.receive_data(address, price, link)
auto_bot.run_bot()