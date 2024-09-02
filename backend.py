from src import index

async def index_document(path: str, collection: str): 
    # Logic to index the document
    doc = index.Document(path, collection)
    doc.load_document()
    doc.index_document()
    doc.save_metadata()
    pass