import time
from importers.reddit import import_reddit_content

from db.setupdb import session
from db.models import Source

def update_reddit(post_url):
    """
    Fetch and update content from a Reddit post.
    """
    print(f"Checking Reddit for updates on: {post_url}")
    try:
        import_reddit_content(post_url)
        print(f"Reddit post {post_url} updated successfully.")
    except Exception as e:
        print(f"Failed to update Reddit content: {e}")

def get_reddit_sources():
    """
    Fetch all Reddit URLs from the database.
    """
    return session.query(Source).filter(Source.base_url == 'reddit').all()

def check_for_new_reddit_content():
    """
    Periodically check for updates to a Reddit post
    """
    reddit_sources = get_reddit_sources()

    if not reddit_sources:
        print("No Reddit sources found.")
        return

    while True:
        print("Checking for Reddit updates...")
        for source in reddit_sources:
            update_reddit(source.url)

        time.sleep(20)
