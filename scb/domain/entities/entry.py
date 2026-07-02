from __future__ import annotations

from dataclasses import dataclass

from scb.domain.identifiers.document_id import DocumentId


@dataclass(frozen=True, slots=True)
class Entry:
    """
    One immutable lore entry extracted from a source document.

    The compiler guarantees that `raw_text` is preserved exactly as it
    appeared in the source document.
    """

    document_id: DocumentId
    entry_number: int
    raw_text: str

    def __post_init__(self) -> None:
        if self.entry_number < 1:
            raise ValueError("entry_number must be greater than zero.")

        if not self.raw_text:
            raise ValueError("raw_text must not be empty.")

    def __str__(self) -> str:
        return self.raw_text
