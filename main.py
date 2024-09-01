from src import config
import backend

from fastapi import FastAPI, HTTPException, Query, Header, BackgroundTasks
from typing import Optional

import uuid
import datetime

app = FastAPI()

@app.get("/ping", tags=["Internal"])
async def ping():
    """
    Ping the server

    :return: 
    """
    return {"ping": "pong", "timestamp": datetime.datetime.now()}


@app.post("/customer", tags=["Internal"])
def onboard_customer(
    customer_id: str = Query(..., title="Customer ID", description="Customer ID"),
):
    """
    Onboard a customer. This will 
    - create a new folder in the s3 bucket for the customer
    - create a new collection in the OpenSearch DB for the customer

    :param customer_id: customer id

    :return: 
    """
    return {"message": "Customer onboarded", "customer_id": customer_id}

@app.delete("/customer", tags=["Internal"])
async def offboard_customer(
    background_tasks: BackgroundTasks,
    customer_id: str = Query(..., title="Customer ID", description="Customer ID"),
):
    """
    Offboard a customer. This will 
    - delete all customer's collections in the OpenSearch DB for the customer
    - delete the folder in the s3 bucket for the customer

    :param customer_id: customer id

    :return: 
    """
    job_id = str(uuid.uuid4())
    # validate the customer id
    # invoke the offboarding method from backend
    return {"message": "", "job_id": job_id}

@app.get("/customer", tags=["Internal"])
def get_customer(
    customer_id: Optional[str] = Query(None, title="Customer ID", description="Customer ID"),
):
    """
    This return a list of collections for a customer. If customer_id is not provided, it will return all customers

    :param customer_id: customer id
    :return:
    """
    # TODO: remember to introduce pagination when we have a lot of customers and lots of collections
    return {"message": "Customer collections retrieved", "customer_id": customer_id, "collections": []}

@app.get("/a/job", tags=["Customer Admin"])
async def get_job_status(job_id: str):
    """
    Get the status of a job

    :param job_id: job id
    
    :return: Job status
    """
    return {"status": "toBeImplemented"}

@app.post("/a/collection", tags=["Customer Admin"])
def create_collection(
    collection: str = Query(..., title="Collection name", description="Collection name"),
):
    """
    Create a collection

    :param collection: collection name

    :return: 
    """
    return {"message": "Collection created", "collection": collection}


@app.post("/a/document", tags=["Customer Admin"])
async def index_document(
    background_tasks: BackgroundTasks,
    path: str = Query(..., title="S3 path", description="S3 path to the document"),
    collection: str = Query(..., title="Collection name", description="Collection to which the document belongs"),
):
    """
    Index a document

    :param path: s3 path to the document

    :param collection: collection name

    :return: 
    """
    job_id = str(uuid.uuid4())
    # validate the path
    # invoke the indexing method from backend
    return {"message": "", "job_id": job_id}

@app.delete("/a/document", tags=["Customer Admin"])
async def deindex_document(
    background_tasks: BackgroundTasks,
    path: str = Query(..., title="S3 path", description="S3 path to the document"),
    collection: str = Query(..., title="Collection name", description="Collection to which the document belongs"),
):
    """
    Remove all the indexed data for a document from the OpenSearch DB

    :param path: s3 path to the document

    :param collection: collection name

    :return: 
    """
    job_id = str(uuid.uuid4())
    # validate the path
    # invoke the deindexing method from backend
    return {"message": "", "job_id": job_id}

@app.get("/u/generate", tags=["User"])
def generate(
    q: str = Query(None, title="Query string", description="Query string to search"),
    collection: str = Query(None, title="Collection name", description="Collection name to search")
):
    """
    Generate response for the query
    
    :param q: query string

    :param collection: collection name
    
    :return: 
    """
    return {"message": "Response generated", "q": q, "collection": collection, "response": "toBeImplemented", "retrieved_documents": []}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")