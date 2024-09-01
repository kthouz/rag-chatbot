from src import config
from src import utils

from typing import List
import boto3

def chunk_document(text: str, chunk_size: int = 1000, chunking_strategy: str=None) -> List[str]:
    # return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    raise NotImplementedError

def generate_embeddings(text: str) -> List[float]:
    raise NotImplementedError

def index_document(text: str, collection: str, metadata: dict):
    embeds = generate_embeddings(text)
    raise NotImplementedError

class Document():
    def __init__(self, s3_path: str, collection: str):
        self.s3_path = s3_path
        self.collection = collection
        self.text = ""
        self.embeddings = []
        self.metadata = {}
    
    def load_document(self):
        # load the document from s3
        self.text = utils.load_file_from_s3(self.s3_path)
    
    def save_metadata(self, metadata: dict = {}):
        # save metadata to the database
        if not metadata:
            metadata = self.metadata
        raise NotImplementedError
    
    def index_document(self):
        # chunk the document to opensearch vector database
        chunks = chunk_document(self.text)
        # generate embeddings
        for chunk in chunks:
            index_document(chunk, self.collection, self.metadata)
