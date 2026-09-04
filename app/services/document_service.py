from ..models.document import Document
from ..repositories.document_repository import DocumentRepository


class DocumentService:
    def __init__(self, repository: DocumentRepository):
        self.repository = repository

    def create(self, document: Document) -> Document:
        document = Document(
            title=document.title,
            content=document.content,
            category=document.category,
            status=document.status,
            created_at=document.created_at,
            updated_at=document.updated_at,
        )
        return self.repository.create(document)

    def find_all(self) -> list[Document]:
        return self.repository.find_all()

    def find_by_id(self, document_id) -> Document | None:
        return self.repository.find_by_id(document_id)

    def update(self, document: Document) -> Document:
        return self.repository.update(document)

    def delete(self, document_id) -> bool:
        return self.repository.delete(document_id)
