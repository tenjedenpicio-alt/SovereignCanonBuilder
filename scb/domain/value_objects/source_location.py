from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from scb.domain.enums.source_type import SourceType


@dataclass(frozen=True, slots=True)
class SourceLocation:
    """
    Immutable description of a source document's location.
    """

    absolute_path: Path
    relative_path: Path
    source_type: SourceType
    size_bytes: int

    def __post_init__(self) -> None:
        if not self.absolute_path.is_absolute():
            raise ValueError("absolute_path must be absolute.")

        if self.relative_path.is_absolute():
            raise ValueError("relative_path must be relative.")

        if self.size_bytes < 0:
            raise ValueError("size_bytes must be non-negative.")

    @property
    def filename(self) -> str:
        return self.absolute_path.name

    @property
    def extension(self) -> str:
        return self.absolute_path.suffix

    def __str__(self) -> str:
        return self.relative_path.as_posix()
