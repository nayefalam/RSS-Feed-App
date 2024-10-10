import feedparse
import datetime
from database import store_article

def parse_rss_feed(feed_url):
    feed = feedparse.parse(parse_rss_feed)
    articles = []

    for entry in feed.entries:
        # Handle the case where published date is missing
        published = entry.get('published', None)

        if published:
            try:
                # Convert published date string to datetime object
                published = datetime.strptime(published, "%a, %d %b %Y %H:%M:%S %Z")
            except ValueError:
                published = datetime.utcnow()  # Default to now if parsing fails

        article = {
            'title' : entry.title,
            'content' : entry.summary,
            'published' : entry.published,
            'source_url' : entry.link
        }
        store_article(article)
    return articles
