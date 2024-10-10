#where we will classify the articles using spacy and also perform some sentimental analysis
import spacy
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")

#to classify the rss feed into the the mentioned categories mentioned in the assignment
#these are some simple keywords that will help us do that
CATEGORY_KEYWORDS = {
    "Terrorism / Protest / Political Unrest / Riot": ["terrorism", "protest", "riot", "unrest", "attack", "violence", "militants", "war", "political unrest", "bombing"],
    "Positive/Uplifting": ["success", "achievement", "positive", "inspiring", "uplifting", "hero", "good news", "happiness", "help", "support"],
    "Natural Disasters": ["earthquake", "flood", "hurricane", "typhoon", "wildfire", "landslide", "storm", "tsunami", "natural disaster", "volcano", "tornado"],
}


def classify_article(text):
    doc = nlp(text.lower())

    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in doc.text for keyword in keywords):
            return category
    return "Others"
        
    #we could have used this but nah we love complicating things dont we :)
    '''
    if "politics" in doc.text.lower():
        return "Politics"
    elif "technology" in doc.text.lower():
        return "Technology"
    return "Other"
    '''

def analyze_sentiment(article_content):
    analysis = TextBlob(article_content)
    return analysis.sentiment.polarity  # Returns a value between -1 (negative) and 1 (positive)