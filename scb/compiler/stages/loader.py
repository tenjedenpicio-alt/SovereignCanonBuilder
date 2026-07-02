from __future__ import annotations

from pathlib import Path

from scb.domain.enums.source_type import SourceType
from scb.domain.value_objects.source_location import SourceLocation

SUPPORTED_EXTENSIONS = {
    SourceType.MARKDOWN,
    SourceType.TEXT,
    SourceType.ODT,
    SourceType.JSONL,
}


def discover_documents(root: Path) -> list[SourceLocation]:
    """
    Recursively discover every supported source document beneath a root directory.
    """

    documents: list[SourceLocation] = []

    for path in sorted(root.rglob("*")):

        if not path.is_file():
            continue

        suffix = path.suffix.lower()

        try:
            source_type = SourceType(suffix)
        except ValueError:
            continue

        if source_type not in SUPPORTED_EXTENSIONS:
            continue

        documents.append(
            SourceLocation(
                absolute_path=path.resolve(),
                relative_path=path.relative_to(root),
                source_type=source_type,
                size_bytes=path.stat().st_size,
            )
        )

    return documents
