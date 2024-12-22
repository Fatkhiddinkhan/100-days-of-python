from bs4 import BeautifulSoup
import requests
url1 = "https://appbrewery.github.io/news.ycombinator.com/"
url2 = "https://news.ycombinator.com/news"
response = requests.get(url=url2)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
article_tags = soup.find_all(name="span", class_="titleline")
article_texts = []
article_urls = []
for article_tag in article_tags:
    anchor_tag = article_tag.find("a")
    article_text = anchor_tag.getText()
    article_texts.append(article_text)
    article_url = anchor_tag.get("href")
    article_urls.append(article_url)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_vote_index = article_upvotes.index(max(article_upvotes))
print(article_texts[max_vote_index])
print(article_urls[max_vote_index])
print(max(article_upvotes))



























# with open(file="./website.html", mode="r") as file:
#     data = file.read()
# soup = BeautifulSoup(data, "html.parser")
# # print(soup.title)
#
# # print(soup.find_all(name="a"))
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     pass
#
# url = soup.select_one(selector="p a")
# # print(url)
#
# contents_url = soup.select(".heading")
# print(contents_url)