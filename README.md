# DYNAMIC DATA EXTRACTION

## Description
This project involved creating a backend dynamic data importer and processor. It is designed to extract, process, and manage data from two sources which are Wikipedia and Reddit. The project involves creating a database which utilizes SQLAlchemy and SQLite. Once the data is fetched from the source, it is cleaned, added to the database and chunked. The project also features real-time updates if the contant has been updated at the source. The project is built with modularity and scalability in mind, with plans for future integration of AI-driven transformations and vector space embedding techniques as well as data collection from more sources

## **Key Features**
- *Content Importers:*
  - Wikipedia Importer: Fetch content from Wikipedia pages by providing URLs.
  - Reddit Importer: Extract data from Reddit posts by providing post URLs.

- *Database Integration:*
  - Powered by *SQLite* (or other databases with minor configuration changes).
  - Supports modular models for storing and retrieving data efficiently.
  - Handles schema updates via Alembic migrations.

- *Export Functionality:*
  - Export data to JSON and CSV formats for further analysis or sharing.

- *Real-Time Content Updates:*
  - Automated update checks for Wikipedia and Reddit sources.
  - Monitors pre-defined sources and fetches new content periodically.

- *Command-Line Interface (CLI):*
  - Fully interactive with --help for detailed guidance.
  - Dynamic inputs for ease of use.

- *Logging and Error Handling:*
  - Comprehensive logging for debugging and process tracking.
  - Handles exceptions gracefully with meaningful error messages.

---


### *Prerequisites*
- Python 3.10 or later
- Virtual environment (venv)
- SQLite (pre-installed with Python)
- Additional Python dependencies listed in requirements.txt


## Project Structure

```
.
├── db
│   ├── models.py         # Database models (Source, Download, Document, Chunk)
│   ├── setupdb.py        # Database setup and session management
│   ├── exporter.py       # Export functionality for data
├── db_diagram
│   ├── Database_diagram.png  # Visual representation of the database schema
│   └── database_diagram.py   # Script to generate the database diagram
├── importers
│   ├── reddit.py         # Imports content from Reddit posts
│   ├── wikipedia.py      # Imports content from Wikipedia pages
├── updaters
│   ├── reddit_updater.py # Updates Reddit content
│   ├── wiki_updater.py   # Updates Wikipedia
├── main.py               # CLI for running the application
├── main.1                # Main entry point of the application
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## How it works

### *Installation*
1. Clone the repository:
   ```bash
   git clone https://github.com/Kagendoooo/Dynamic_data_extraction.git
   ```
2. Move into the virtual environment:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
3. Move into the directory:
   ```bash
   cd Dynamic_data_exctraction
   ```
4. Install the dependencies from the requirements.txt file.

### Database setup
- Setup the database using:
  ```bash 
  python main.py --setup_db
   ```

### Data importing
1. Importing data from Wikipedia:
   ```bash
   python main.py --import_wikipedia (URL here)
   ```

2. Importing data from Reddit:
    ```bash
    python main.py --import_reddit (URL here)
    ```

### Data exportation
- The data collected is the exported to the database using:
   ```bash
   python main.py --export_data
   ```

### Check for updates

1. Check for Wikipedia updates:
   ```bash
   python main.py --check_for_wikipedia_updates
   ```

2. Check for Reddit updates:
   ```bash
   python main.py --check_for_reddit_updates
   ```



## Code review

### Database Models (`db/models.py`)

- **Source**: Represents a content source (e.g. Wikipedia, Reddit).
- **Download**: Tracks downloaded content from a source.
- **Document**: Stores the content of a download.
- **Chunk**: Represents a portion of a document for easier processing.

### Importers

- **`wikipedia.py`**: Fetches content from Wikipedia pages using the MediaWiki API.
- **`reddit.py`**: Fetches content from Reddit posts in JSON format.

### Exporter (`db/exporter.py`)

- Exports data from the database to CSV and JSON formats.

### CLI (`main.py`)

- The CLI allows you to interact with the project through various command-line arguments.

### Updaters

- **`wiki_updater.py`**: Periodically check for updates to monitored Wikipedia pages.
- **`reddit_updater.py`**: Periodically check for updates to monitored Reddit posts. 

### Man file (`main.1`)

- This contains the user manual for the `main.py` file.

###  Db_diagram

- **`database_diagram.py`**: This was used to create the database diagram
- **`Database_diagram.png`**: The database diagram generated


## Technologies Used
- Python: Core programming language.
- SQLAlchemy: ORM for database management.
- SQLite: Lightweight relational database for local storage.
- Requests: HTTP client for interacting with APIs.
- Logging: For debugging and tracking application processes.
- Pygraphviz: Generates database diagram.



## AUTHORS
1. Simon Kamundia - simonkamundia8@gmail.com
2. Nicole Maina - kagendonikki16@gmail.com
