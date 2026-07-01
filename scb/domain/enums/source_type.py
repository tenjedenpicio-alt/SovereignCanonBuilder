from __future__ import annotations

from enum import Enum


class SourceType(str, Enum):
    """
    Supported source document formats.
    """

    MARKDOWN = ".md"
    JSONL = ".jsonl"
    TEXT = ".txt"
    ODT = ".odt"

    @property
    def extension(self) -> str:
        return self.value
