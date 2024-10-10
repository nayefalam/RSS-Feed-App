from feedparse import parse_rss_feed
from tasks import process_article

RSS_FEEDS = ["http://feeds.foxnews.com/foxnews/politics"]

def run_app():
    for feed in RSS_FEEDS:
        articles = parse_rss_feed(feed)
        for article in articles:
            process_article.delay(article)

if __name__ == "__main__":
    run_app()