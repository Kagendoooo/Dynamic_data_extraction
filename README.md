# DYNAMIC DATA EXTRACTION

## Description
This project involved creating a backend dynamic data importer and processor. We designed it to extract, process, and manage data from two sources which were Wikipedia and Reddit. The project involves creating a database which utilizes SQLAlchemy and SQLite. Once the data is fetched from the source, it is cleaned, added to the database and chunked. 

## Features

- Import content from:
  - WordPress posts
  - Wikipedia pages
  - Reddit posts
- Export data to CSV and JSON formats
- Check for updates from existing sources
- Set up and manage a SQLite database

## Requirements

- Python 3.8+
- SQLite
- Libraries:
  - `sqlalchemy`
  - `requests`
  - `beautifulsoup4`
  - `argparse`
  - `logging`

Install the required libraries using:
```bash
pip install -r requirements.txt
```

## Project Structure

```
.
├── db
│   ├── models.py         # Database models (Source, Download, Document, Chunk)
│   ├── setup.py          # Database setup and session management
│   └── exporter.py       # Export functionality for data
├── importers
│   ├── reddit_importer.py  # Imports content from Reddit posts
│   ├── wiki_importer.py    # Imports content from Wikipedia pages
│   └── wp_importer.py      # Imports content from WordPress posts
├── updaters
│   └── source_updater.py   # Checks for updates from existing sources
├── main.py               # CLI for running the application
└── requirements.txt      # Python dependencies
```

## Usage

### Setting Up the Database

Before importing content, set up the database:
```bash
python main.py --setup_db
```

### Importing Content

#### Import WordPress Content
```bash
python main.py --import_wp
```

#### Import Wikipedia Content
```bash
python main.py --import_wikipedia <Wikipedia_URL>
```

#### Import Reddit Content
```bash
python main.py --import_reddit <Reddit_URL>
```

#### Import Dynamic WordPress Content
```bash
python main.py --dynamic_wp_importer <WordPress_URL>
```

### Checking for Updates

To check for new content updates:
```bash
python main.py --check_for_updates
```

### Exporting Data

To export data to CSV and JSON:
```bash
python main.py --export_data
```

## Code Overview

### Database Models (`db/models.py`)

- **Source**: Represents a content source (e.g., WordPress, Wikipedia, Reddit).
- **Download**: Tracks downloaded content from a source.
- **Document**: Stores the content of a download.
- **Chunk**: Represents a portion of a document for easier processing.

### Importers

- **`wp_importer.py`**: Fetches content from WordPress posts using a base URL and post slug.
- **`wiki_importer.py`**: Fetches content from Wikipedia pages using the MediaWiki API.
- **`reddit_importer.py`**: Fetches content from Reddit posts in JSON format.

### Exporter (`db/exporter.py`)

Exports data from the database to CSV and JSON formats.

### CLI (`main.py`)

The CLI allows you to interact with the project through various command-line arguments.

## Logging

Logs are displayed in the console to track the progress and debug issues.

## Future Enhancements

- Add support for more content sources.
- Implement advanced data analysis and visualization tools.
- Add a web-based user interface for easier management.

## License

This project is licensed under the MIT License.

---

Feel free to contribute or raise issues for further improvements!


