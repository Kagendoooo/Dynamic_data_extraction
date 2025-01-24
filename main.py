"""Main entry point for the application"""
import argparse
from db.setupdb import setup_database, session
from importers.wikipedia import import_wikipedia_content
from importers.reddit import import_reddit_content
from db.exporter import export_data
import re

def is_valid_url(url):
    """
    Validates whether the provided string is a valid URL.
    """
    url_regex = re.compile(
        r'^(https?://)'
        r'([a-zA-Z0-9.-]+)'
        r'(\.[a-zA-Z]{2,})'
        r'(/.*)?$',
        re.IGNORECASE
    )
    return re.match(url_regex, url) is not None


def main():
    """
    This  script serves as a comand line tool for importing and processing the sources and data motification
    """

    parser = argparse.ArgumentParser(description='Content Importer and Processor')
    parser.add_argument('--setup_db', help='Set up the database', action='store_true')
    parser.add_argument('--import_wikipedia', help='Import content from a Wikipedia page URL', action='store_true')
    parser.add_argument('--export_data', help='Export data to CSV and JSON', action='store_true')
    parser.add_argument('--import_reddit', help='Import content from a Reddit post URL', action='store_true')
    args = parser.parse_args()

    # Set up the database if the argument is passed
    if args.setup_db:
        setup_database()
        print("Database setup completed!")
        return

    # Request user to provide Wikipedia URL
    if args.import_wikipedia:
        while True:
            wikipedia_url = input("Please insert Wikipedia URL: ").strip()
            if is_valid_url(wikipedia_url):
                import_wikipedia_content(wikipedia_url)
                print("Content from Wikipedia page imported successfully!")
                break
            else:
                print("Please provide a valid URL.")

    # Request user to input Reddit post URL
    if args.import_reddit:
        while True:
            reddit_url = input("Please insert Reddit URL: ").strip()
            if is_valid_url(reddit_url):
                import_reddit_content(reddit_url)
                print("Content from Reddit post imported successfully!")
                break
            else:
                print("Please provide a valid URL.")

    # Exports and saves data from the database as JSON and CSV
    if args.export_data:
        export_data(session, export_to_csv=True, export_to_json=True)
        print("Data exported successfully to CSV and JSON files!")

if __name__ == '__main__':
    main()
