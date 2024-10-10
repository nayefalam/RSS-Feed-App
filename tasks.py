from celery import Celery
from classifier import classify_article
from database import store_article

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def process_article(article):
    category = classify_article(article['content'])
    article['category'] = category
    store_article(article)
