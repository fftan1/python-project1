from fastapi import APIRouter

from ..schemas import document_schema
from ..services.document_service import DocumentService

router = APIRouter(prefix="/documents", tags=["documents"])


def create_document_router(document_service: DocumentService):
    @router.get("/")
    def get_documents():
        documents = document_service.find_all()
        return documents

    @router.post("/")
    def create_document(request: document_schema.BaseRequest):
        return document_service.create(request)

    return router
