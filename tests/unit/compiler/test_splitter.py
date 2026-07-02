from pathlib import Path

from scb.compiler.stages.splitter import split_document
from scb.domain.entities.document import Document
from scb.domain.enums.source_type import SourceType
from scb.domain.identifiers.document_id import DocumentId
from scb.domain.value_objects.checksum import Checksum
from scb.domain.value_objects.source_location import SourceLocation

VALID_SHA256 = (
    "0123456789abcdef"
    "0123456789abcdef"
    "0123456789abcdef"
    "0123456789abcdef"
)


def make_document(text: str) -> Document:
    return Document(
        document_id=DocumentId("lore"),
        source_location=SourceLocation(
            absolute_path=Path.cwd() / "lore.md",
            relative_path=Path("lore.md"),
            source_type=SourceType.MARKDOWN,
            size_bytes=len(text),
        ),
        checksum=Checksum(VALID_SHA256),
        raw_text=text,
    )


def test_split_two_entries() -> None:
    text = (
        "LORE_SCHEMA_ENTRY:\n"
        "ENTITY_ID: one\n"
        "\n"
        "LORE_SCHEMA_ENTRY:\n"
        "ENTITY_ID: two\n"
    )

    document = make_document(text)

    entries = split_document(document)

    assert len(entries) == 2

    assert entries[0].entry_number == 1
    assert entries[1].entry_number == 2

    assert entries[0].raw_text.startswith("LORE_SCHEMA_ENTRY:")
    assert entries[1].raw_text.startswith("LORE_SCHEMA_ENTRY:")


def test_document_without_entries_returns_empty_list() -> None:
    document = make_document("Hello world")

    assert split_document(document) == []


def test_splitter_preserves_text_exactly() -> None:
    text = (
        "LORE_SCHEMA_ENTRY:\n"
        "ENTITY_ID: one\n"
        "\n"
        "Paragraph.\n"
        "\n"
    )

    document = make_document(text)

    entries = split_document(document)

    assert entries[0].raw_text == text
