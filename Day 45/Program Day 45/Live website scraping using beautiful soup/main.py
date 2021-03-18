import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/")

data = response.text

soup = BeautifulSoup(data, "html.parser")

articles = soup.find_all(name="a", class_="storylink")

articles_text = []
articles_link = []

for article_tag in articles:
    text = article_tag.getText()
    link = article_tag.get("href")
    articles_text.append(text)
    articles_link.append(link)

articles_vote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

highest_vote = articles_vote.index(max(articles_vote))

print(f"{articles_text[highest_vote]}\n{articles_link[highest_vote]}\n{articles_vote[highest_vote]}")
