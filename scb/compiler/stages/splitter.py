from __future__ import annotations

from scb.domain.entities.document import Document
from scb.domain.entities.entry import Entry

_ENTRY_MARKER = "LORE_SCHEMA_ENTRY:"


def split_document(document: Document) -> list[Entry]:
    """
    Split a Document into immutable Entry objects.

    The splitter preserves every character exactly as it appeared in the
    source document.
    """

    text = document.raw_text

    starts: list[int] = []

    position = text.find(_ENTRY_MARKER)

    while position != -1:
        starts.append(position)
        position = text.find(_ENTRY_MARKER, position + len(_ENTRY_MARKER))

    if not starts:
        return []

    entries: list[Entry] = []

    for number, start in enumerate(starts, start=1):
        end = starts[number] if number < len(starts) else len(text)

        raw = text[start:end]

        entries.append(
            Entry(
                document_id=document.document_id,
                entry_number=number,
                raw_text=raw,
            )
        )

    return entries
