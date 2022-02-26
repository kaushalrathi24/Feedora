import feedparser
from bs4 import BeautifulSoup
import mysql.connector as sql
import time
import json
import datetime

mydb = sql.connect(
    host='localhost',
    user='root',
    passwd='oneminutenineseconds',
    database='news')

cursor = mydb.cursor()


def verge():
    feed = feedparser.parse('https://www.theverge.com/tech/rss/index.xml')
    for entry in feed.entries:
        article = {}
        article['link'] = entry.link
        if (article['link'], ) not in links:
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
            mydb.commit()


def toi(link, topic):
    feed = feedparser.parse(link)
    for entry in feed.entries:
        article = {}
        article['link'] = entry.link
        if (article['link'], ) not in links:
            article['title'] = entry.title
            pub_date = entry.published.split(" ")[1:5]
            pub_date[1] = datetime.datetime.strptime(
                pub_date[1], "%b").strftime("%m")
            article['pub_date'] = "-".join(pub_date[-2:-5:-1]) + \
                " " + pub_date[3] + "+05:30"
            content = BeautifulSoup(entry.summary, 'lxml')
            article['description'] = content.getText() + "..."
            article['outlet'] = "TOI"
            query = "insert into articles values(%s, %s, %s, %s, %s)"
            args = (article['link'], json.dumps(article),
                    article['pub_date'], topic, 'toi')
            cursor.execute(query, args)
            mydb.commit()


def bbc(link, topic):
    feed = feedparser.parse(link)
    for entry in feed.entries:
        article = {}
        article["link"] = entry.link
        if (article['link'], ) not in links:
            article["title"] = entry.title
            pub_date = entry.published.split(" ")[1:5]
            pub_date[1] = datetime.datetime.strptime(
                pub_date[1], "%b").strftime("%m")
            article['pub_date'] = "-".join(pub_date[-2:-5:-1]) + \
                " " + pub_date[3] + "+00:00"
            article["description"] = entry.summary + "..."
            article['outlet'] = "BBC"
            query = "insert into articles values(%s, %s, %s, %s, %s)"
            args = (article['link'], json.dumps(article),
                    article['pub_date'], topic, 'bbc')
            cursor.execute(query, args)
            mydb.commit()


def wion(link, topic):
    feed = feedparser.parse(link)
    for entry in feed.entries:
        article = {}
        article["link"] = entry.link
        if (article['link'], ) not in links:
            article["title"] = entry.title
            pub_date = entry.published.split(" ")[1:5]
            pub_date[1] = datetime.datetime.strptime(
                pub_date[1], "%b").strftime("%m")
            article['pub_date'] = "-".join(pub_date[-2:-5:-1]) + \
                " " + pub_date[3] + "+05:30"
            article["description"] = entry.summary + "..."
            article['outlet'] = "WION"
            query = "insert into articles values(%s, %s, %s, %s, %s)"
            args = (article['link'], json.dumps(article),
                    article['pub_date'], topic, 'wion')
            cursor.execute(query, args)
            mydb.commit()


def ndtv(link, topic):
    feed = feedparser.parse(link)
    for entry in feed.entries:
        article = {}
        article["link"] = entry.link
        if (article['link'], ) not in links:
            article["title"] = entry.title
            pub_date = entry.published.split(" ")[1:5]
            pub_date[1] = datetime.datetime.strptime(
                pub_date[1], "%b").strftime("%m")
            article['pub_date'] = "-".join(pub_date[-2:-5:-1]) + \
                " " + pub_date[3] + "+05:30"
            article["description"] = entry.summary + "..."
            article['outlet'] = "NDTV"
            query = "insert into articles values(%s, %s, %s, %s, %s)"
            args = (article['link'], json.dumps(article),
                    article['pub_date'], topic, 'ndtv')
            cursor.execute(query, args)
            mydb.commit()


def hindu(link, topic):
    feed = feedparser.parse(link)
    for entry in feed.entries:
        article = {}
        article["link"] = entry.link
        if (article['link'], ) not in links:
            article["title"] = entry.title
            pub_date = entry.published.split(" ")[1:5]
            pub_date[1] = datetime.datetime.strptime(
                pub_date[1], "%b").strftime("%m")
            article['pub_date'] = "-".join(pub_date[-2:-5:-1]) + \
                " " + pub_date[3] + "+05:30"
            article["description"] = entry.summary + "..."
            article['outlet'] = "The Hindu"
            query = "insert into articles values(%s, %s, %s, %s, %s)"
            args = (article['link'], json.dumps(article),
                    article['pub_date'], topic, 'hindu')
            cursor.execute(query, args)
            mydb.commit()


while True:
    cursor.execute(
        "delete from articles where pub_date < DATE_SUB(NOW() , INTERVAL 5 DAY)")
    mydb.commit()
    cursor.execute("select link from articles")
    links = cursor.fetchall()
    verge()

    toi("https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms", "india_news")
    toi('https://timesofindia.indiatimes.com/rssfeeds/296589292.cms', 'world_news')
    toi('https://timesofindia.indiatimes.com/rssfeeds/1898055.cms', 'economy')
    toi('https://timesofindia.indiatimes.com/rssfeeds/4719148.cms', 'sports')
    toi('https://timesofindia.indiatimes.com/rssfeeds/3908999.cms', 'health')
    toi('https://timesofindia.indiatimes.com/rssfeeds/66949542.cms', 'tech')
    toi('https://timesofindia.indiatimes.com/rssfeeds/1081479906.cms', 'entertainment')

    bbc('http://feeds.bbci.co.uk/news/world/rss.xml', 'world_news')
    bbc('http://feeds.bbci.co.uk/news/business/rss.xml', 'economy')
    bbc('http://feeds.bbci.co.uk/news/health/rss.xml', 'health')
    bbc('http://feeds.bbci.co.uk/news/technology/rss.xml', 'tech')
    bbc('http://feeds.bbci.co.uk/sport/rss.xml', 'sports')
    bbc('http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'entertainment')

    wion('https://www.wionews.com/feeds/world/rss.xml', 'world_news')
    wion('https://www.wionews.com/feeds/business-economy/rss.xml', 'economy')
    wion('https://www.wionews.com/feeds/sports/rss.xml', 'sports')
    wion('https://www.wionews.com/feeds/science-technology/rss.xml', 'tech')
    wion('https://www.wionews.com/feeds/india-news/rss.xml', 'india_news')
    wion('https://www.wionews.com/feeds/entertainment/rss.xml', 'entertainment')

    ndtv('https://feeds.feedburner.com/ndtvnews-world-news?format=xml', 'world_news')
    ndtv('https://feeds.feedburner.com/ndtvprofit-latest?format=xml', 'economy')
    ndtv('https://feeds.feedburner.com/gadgets360-latest?format=xml', 'tech')
    ndtv('https://feeds.feedburner.com/ndtvmovies-latest?format=xml', 'entertainment')
    ndtv('https://feeds.feedburner.com/ndtvnews-india-news?format=xml', 'india_news')
    ndtv('https://feeds.feedburner.com/ndtvsports-latest?format=xml', 'sports')

    hindu('https://www.thehindu.com/news/international/feeder/default.rss', 'world_news')
    hindu('https://www.thehindu.com/news/national/feeder/default.rss', 'india_news')
    hindu('https://www.thehindu.com/business/feeder/default.rss', 'economy')
    hindu('https://www.thehindu.com/sport/feeder/default.rss', 'sports')
    hindu('https://www.thehindu.com/life-and-style/fitness/feeder/default.rss', 'health')
    hindu('https://www.thehindu.com/entertainment/feeder/default.rss', 'entertainment')

    time.sleep(1800)
