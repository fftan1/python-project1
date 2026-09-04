from dataclasses import dataclass


@dataclass
class Document:
    id: int
    title: str
    content: str
    category: str
    status: str
    created_at: str
    updated_at: str

    def publish(self):
        if self.status == "archived":
            raise ValueError("Archived document cannot be published")

        self.status = "published"

    def archive(self):
        if self.status == "published":
            raise ValueError("Published document cannot be archived")

        self.status = "archived"
