import pytest

from scb.domain.entities.entry import Entry
from scb.domain.identifiers.document_id import DocumentId


def test_valid_entry() -> None:
    entry = Entry(
        document_id=DocumentId("lore"),
        entry_number=1,
        raw_text="LORE_SCHEMA_ENTRY:\nENTITY_ID: test",
    )

    assert entry.entry_number == 1
    assert str(entry) == "LORE_SCHEMA_ENTRY:\nENTITY_ID: test"


def test_entry_number_must_be_positive() -> None:
    with pytest.raises(ValueError):
        Entry(
            document_id=DocumentId("lore"),
            entry_number=0,
            raw_text="abc",
        )


def test_raw_text_must_not_be_empty() -> None:
    with pytest.raises(ValueError):
        Entry(
            document_id=DocumentId("lore"),
            entry_number=1,
            raw_text="",
        )
