from sqlalchemy import Column, String, Text, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
import datetime


# Base class for all models
Base = declarative_base()

class Article(Base):

    #Defines the Article table schema.
    __tablename__ = 'articles'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)  # Title of the article
    content = Column(Text, nullable=False)  # Main content of the article
    published = Column(DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))  # Date published
    source_url = Column(String, nullable=False, unique=True)  # Source URL of the article (must be unique)
    category = Column(String, nullable=True)  # The category the article is classified into
    
    def __repr__(self):
        return f"<Article(title={self.title}, category={self.category})>"
