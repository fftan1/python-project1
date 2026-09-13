import pytest

from app.enum.status import StatusEnum
from app.models.document import Document

document = Document(
    id=1,
    title="Test Document",
    content="This is a test document.",
    category="Test",
    created_at="2023-01-01",
    updated_at="2023-01-01",
    status=StatusEnum.DRAFT,
)


def test_publish():
    document.publish()
    assert document.status == StatusEnum.PUBLISHED


def test_archive():
    document.archive()
    assert document.status == StatusEnum.ARCHIVED


def test_archive_already_archived():
    with pytest.raises(
        ValueError, match="Cannot published a document that is already archived."
    ):
        document.archive()
