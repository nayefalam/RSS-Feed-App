# Incomplete implementation of utils code for Logging etc!!!

import logging
from datetime import datetime

# Set up logging
def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger()

logger = setup_logging()

# Function to handle errors
def handle_error(error):
    logger.error(f"An error occurred: {error}")

# Validate if the article data has required fields
def is_valid_article(article):
    required_fields = ['title', 'content', 'published', 'url']
    return all(field in article for field in required_fields)

# Format article for display
def format_article(article):
    return f"{article['title']} (Published on {article['published']})"

# Function to format date
def format_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S').strftime('%B %d, %Y')
