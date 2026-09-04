from ..models.document import Document


class DocumentRepository:
    def __init__(self):
        self.documents: list[Document] = []

    def create(self, document: Document) -> Document:
        self.documents.append(document)
        return document

    def find_all(self) -> list[Document]:
        return self.documents

    def find_by_id(self, document_id) -> Document | None:
        for doc in self.documents:
            if doc.id == document_id:
                return doc
        return None

    def update(self, document: Document) -> Document:
        existing_document = self.find_by_id(document.id)
        if not existing_document:
            raise ValueError(f"Document with Id {document.id} not found")
        existing_document.title = document.title
        existing_document.content = document.content
        existing_document.category = document.category
        existing_document.status = document.status
        existing_document.updated_at = document.updated_at
        return existing_document

    def delete(self, document_id) -> bool:
        document = self.find_by_id(document_id)

        if not document:
            raise ValueError(f"Document with ID {document_id} not found")
        self.documents.remove(document)
        return True
