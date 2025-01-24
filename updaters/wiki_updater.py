import time
from importers.wikipedia import import_wikipedia_content
from db.setupdb import session
from db.models import Source

def update_wikipedia(page_url):
    """
    Fetch and update content from a Wikipedia page
    """
    print(f"Checking Wikipedia for updates on: {page_url}")
    try:
        import_wikipedia_content(page_url)
        print(f"Wikipedia page {page_url} updated successfully.")
    except Exception as e:
        print(f"Failed to update Wikipedia content: {e}")

def get_wikipedia_sources():
    """
    Fetch all Wikipedia URLs from the database
    """
    return session.query(Source).filter(Source.base_url == 'wikipedia').all()

def check_for_new_wikipedia_content():
    """
    Periodically check for updates to Wikipedia content
    """
    wikipedia_sources = get_wikipedia_sources()
    
    if not wikipedia_sources:
        print("No Wikipedia sources found.")
        return
    
    while True:
        print("Checking for Wikipedia updates...")
        for source in wikipedia_sources:
            update_wikipedia(source.url)

        time.sleep(20) 
