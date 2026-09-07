from fastapi import FastAPI

from .repositories.document_repository import DocumentRepository
from .routers.document_router import create_document_router
from .services.document_service import DocumentService

app = FastAPI()

document_repository = DocumentRepository()
document_service = DocumentService(document_repository)

document_router = create_document_router(document_service)

app.include_router(document_router)
