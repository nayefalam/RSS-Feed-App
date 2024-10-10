from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from model import Base, Article

# Configuration (you could load this from config.py)
DATABASE_URL = "postgresql://postgres:nayef@localhost/rssfeed"

# Create an engine that manages the database connection
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables if they don't exist
def init_db():
    try:
        Base.metadata.create_all(bind=engine)
        print("Database initialized successfully!")
    except SQLAlchemyError as e:
        print(f"Error initializing database: {e}")

# Dependency for managing a database session
def store_article(article_data):
    session = SessionLocal()
    new_article = Article(**article_data)  

    try:
        session.add(new_article)  # Add the new article to the session
        session.commit()  # Commit the transaction
        print(f"Article '{new_article.title}' stored in the database.")
    except SQLAlchemyError as e:
        session.rollback()  # Rollback in case of error
        print(f"Error storing the article: {e}")
    finally:
        session.close()  # Always close the session
