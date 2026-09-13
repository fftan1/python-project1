from dataclasses import dataclass

from app.enum.status import StatusEnum


@dataclass
class Document:
    id: int
    title: str
    content: str
    category: str
    created_at: str
    updated_at: str
    status: StatusEnum

    def publish(self):
        if self.status == StatusEnum.DRAFT:
            self.status = StatusEnum.PUBLISHED

    def archive(self):
        if self.status == StatusEnum.ARCHIVED:
            raise ValueError("Cannot published a document that is already archived.")
        self.status = StatusEnum.ARCHIVED
