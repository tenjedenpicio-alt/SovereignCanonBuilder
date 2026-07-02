from __future__ import annotations

from dataclasses import dataclass

from scb.domain.identifiers.document_id import DocumentId
from scb.domain.value_objects.checksum import Checksum
from scb.domain.value_objects.source_location import SourceLocation


@dataclass(frozen=True, slots=True)
class Document:
    """
    Immutable source document loaded from disk.
    """

    document_id: DocumentId
    source_location: SourceLocation
    checksum: Checksum
    raw_text: str

    def __post_init__(self) -> None:
        if not self.raw_text:
            raise ValueError("Document must contain text.")
