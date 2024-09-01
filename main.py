from fastapi import FastAPI, HTTPException, Query, Header, BackgroundTasks
from typing import Optional
import uvicorn
import uuid
import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = FastAPI()

@app.get("/ping", tags=["Internal"])
async def ping():
    """
    Ping the server

    :return: 
    """
    return {"ping": "pong", "timestamp": datetime.datetime.now()}

@app.post("/document", tags=["Document"])
def index_document(
    background_tasks: BackgroundTasks, 
    path: str = Query(..., title="Path to the document", description="Path to the document to be indexed", example="/path/to/document"), 
    collection: str = Query(..., title="Collection", description="Collection to which the document belongs", example="collection1")
    ):
    """
    Index a document

    :param path: Path to the document
    :param collection: Collection to which the document belongs
    :return: 
    """
    # Logic to index the document
    logger.info(f"Indexing document {path} in collection {collection}")
    return {"status": "Document indexing started", "document_id": str(uuid.uuid4())}

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8080)