from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base

# Create the database engine
engine = create_engine('sqlite:///project.db', echo=True)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create the session object (global)
session = Session()


def setup_database():
    """Set up the database schema."""
    Base.metadata.create_all(engine)
