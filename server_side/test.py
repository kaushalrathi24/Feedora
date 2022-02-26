import feedparser
from bs4 import BeautifulSoup
import mysql.connector as sql
import time
import json
import datetime

'''def verge(current_entries):
    feed = feedparser.parse('https://www.theverge.com/tech/rss/index.xml')
    for entry in feed.entries:
        article = {}
        article['link'] = entry.link
        if (article['link'], ) not in current_entries:
            article['title'] = entry.title
            article['pub_date'] = entry.published.replace("T", " ")
            content = BeautifulSoup(entry.summary, 'lxml')
            article['description'] = ' '.join(
                [para.getText() for para in content.findAll('p')])
            article['outlet'] = 'The Verge'
            query = "insert into articles values(%s, %s, %s, %s, %s)"
            args = (article['link'], json.dumps(article),
                    article['pub_date'], 'tech', 'verge')
            cursor.execute(query, args)
            mydb.commit()'''


def ndtv():
    feed = feedparser.parse(
        "https://feeds.feedburner.com/ndtvnews-world-news?format=xml")
    entry = feed.entries[0]
    article = {}
    article["link"] = entry.link
    article["title"] = entry.title
    pub_date = entry.published.split(" ")[1:5]
    pub_date[1] = datetime.datetime.strptime(
        pub_date[1], "%b").strftime("%m")
    article['pub_date'] = "-".join(pub_date[:3]) + \
        " " + pub_date[3] + "+05:30"
    article["description"] = entry.summary + "..."
    article['outlet'] = "NDTV"
    return article


print(ndtv())
