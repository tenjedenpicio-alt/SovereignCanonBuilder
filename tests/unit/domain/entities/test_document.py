import hashlib
from pathlib import Path

import pytest

from scb.domain.entities.document import Document
from scb.domain.enums.source_type import SourceType
from scb.domain.identifiers.document_id import DocumentId
from scb.domain.value_objects.checksum import Checksum
from scb.domain.value_objects.source_location import SourceLocation


def make_location() -> SourceLocation:
    return SourceLocation(
        absolute_path=Path.cwd() / "Lore.md",
        relative_path=Path("Lore.md"),
        source_type=SourceType.MARKDOWN,
        size_bytes=10,
    )


def test_document_creation() -> None:
    text = "# Lore"

    checksum = hashlib.sha256(text.encode()).hexdigest()

    document = Document(
        document_id=DocumentId("lore"),
        source_location=make_location(),
        checksum=Checksum(checksum),
        raw_text=text,
    )

    assert document.raw_text == "# Lore"
    assert document.document_id.value == "lore"


def test_document_must_not_be_empty() -> None:
    checksum = hashlib.sha256(b"").hexdigest()

    with pytest.raises(ValueError):
        Document(
            document_id=DocumentId("empty"),
            source_location=make_location(),
            checksum=Checksum(checksum),
            raw_text="",
        )
