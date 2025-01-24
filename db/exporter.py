import csv
import json
from db.models import Chunk
from sqlalchemy.orm import Session
from bs4 import BeautifulSoup


"""
This is how the content is exported from the source to the database
The data is first cleaned, exported then chunked
"""

def clean_html(content):
    """Remove HTML tags from downloaded content."""
    soup = BeautifulSoup(content, 'html.parser')
    return soup.get_text()

def export_data(session: Session, export_to_csv=False, export_to_json=False):
    """Export data to CSV and/or JSON."""
    if export_to_csv:
        with open('chunks_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['id', 'content', 'document_id', 'start_position', 'end_position'])  # CSV header
            
            """Fetch all chunks data"""
            chunks = session.query(Chunk).all()
            for chunk in chunks:
                writer.writerow([chunk.id, chunk.content, chunk.document_id, chunk.start_position, chunk.end_position])
        print("CSV file has been exported successfully.")
    
    if export_to_json:
        chunks_data = []
        
        # Fetch all chunks data
        chunks = session.query(Chunk).all()
        for chunk in chunks:
            chunks_data.append({
                'id': chunk.id,
                'content': clean_html(chunk.content),
                'document_id': chunk.document_id,
                'start_position': chunk.start_position,
                'end_position': chunk.end_position
            })
        
        with open('chunks_data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(chunks_data, jsonfile, ensure_ascii=False, indent=4)
        print("JSON has been file exported successfully.")
