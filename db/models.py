from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

"""This is the base class for all models"""
Base = declarative_base()


"""
This is the source of the downloads
Contains the id, name of download and the base_url
Related to the downloads table through id
"""
class Source(Base):
    __tablename__ = 'sources'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    base_url = Column(String, nullable=False)
    
    downloads = relationship('Download', back_populates='source')


"""
These are downloads from the source
The source_id is unique to each source
"""
class Download(Base):
    __tablename__ = 'downloads'
    
    id = Column(Integer, primary_key=True)
    source_id = Column(Integer, ForeignKey('sources.id'))
    url = Column(String, nullable=False)
    
    source = relationship('Source', back_populates='downloads')
    documents = relationship('Document', back_populates='download')


"""
This is the document obtained from a download
The download_id is unique to each download
"""
class Document(Base):
    __tablename__ = 'documents'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    download_id = Column(Integer, ForeignKey('downloads.id'))
    
    download = relationship('Download', back_populates='documents')
    chunks = relationship('Chunk', back_populates='document')


"""
This is the chunk of a document
It shows where the breaks of the doc start and stop
"""
class Chunk(Base):
    __tablename__ = 'chunks'
    
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    document_id = Column(Integer, ForeignKey('documents.id'))
    start_position = Column(Integer, nullable=False)
    end_position = Column(Integer, nullable=False)
    
    document = relationship('Document', back_populates='chunks')
