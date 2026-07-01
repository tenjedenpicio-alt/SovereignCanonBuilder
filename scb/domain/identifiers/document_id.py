from __future__ import annotations

import re
from dataclasses import dataclass

_VALID_DOCUMENT_ID = re.compile(r"^[A-Za-z0-9_.-]{1,255}$")


@dataclass(frozen=True, slots=True)
class DocumentId:
    """
    Immutable identifier for a source document.

    A DocumentId uniquely identifies a document within a compilation.
    It is independent of filenames, file paths, and checksums.
    """

    value: str

    def __post_init__(self) -> None:
        if self.value != self.value.strip():
            raise ValueError(
                "DocumentId must not contain leading or trailing whitespace."
            )

        if not _VALID_DOCUMENT_ID.fullmatch(self.value):
            raise ValueError(
                f"Invalid DocumentId: {self.value!r}. "
                "Only letters, digits, '_', '-', and '.' are permitted."
            )

    def __str__(self) -> str:
        return self.value
