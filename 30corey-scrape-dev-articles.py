# api_to_csv.py
# Practice: Fetch public API data and save it to CSV

import csv
import requests
from datetime import datetime

url = "https://hn.algolia.com/api/v1/search_by_date"
params = {
    "query": "python developer",
    "tags": "story",
    "hitsPerPage": 20
}

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()
articles = data["hits"]

today = datetime.now().strftime("%Y-%m-%d")

with open("tech_articles_today.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["scrape_date", "headline", "author", "created_at", "article_link", "source"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for article in articles:
        writer.writerow({
            "scrape_date": today,
            "headline": article.get("title"),
            "author": article.get("author"),
            "created_at": article.get("created_at"),
            "article_link": article.get("url"),
            "source": "Hacker News Algolia API"
        })

print("CSV file created: tech_articles_today.csv")