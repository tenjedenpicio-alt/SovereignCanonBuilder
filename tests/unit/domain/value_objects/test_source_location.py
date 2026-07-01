from pathlib import Path

import pytest

from scb.domain.enums.source_type import SourceType
from scb.domain.value_objects.source_location import SourceLocation


def test_valid_source_location() -> None:
    location = SourceLocation(
        absolute_path=Path.cwd() / "tmp" / "lore.md",
        relative_path=Path("history/lore.md"),
        source_type=SourceType.MARKDOWN,
        size_bytes=1024,
    )

    assert location.filename == "lore.md"
    assert location.extension == ".md"
    assert str(location) == "history/lore.md"


def test_absolute_path_must_be_absolute() -> None:
    with pytest.raises(ValueError):
        SourceLocation(
            absolute_path=Path("lore.md"),
            relative_path=Path("history/lore.md"),
            source_type=SourceType.MARKDOWN,
            size_bytes=1,
        )


def test_relative_path_must_be_relative() -> None:
    with pytest.raises(ValueError):
        SourceLocation(
            absolute_path=Path("/tmp/lore.md"),
            relative_path=Path("/history/lore.md"),
            source_type=SourceType.MARKDOWN,
            size_bytes=1,
        )


def test_negative_size_not_allowed() -> None:
    with pytest.raises(ValueError):
        SourceLocation(
            absolute_path=Path("/tmp/lore.md"),
            relative_path=Path("history/lore.md"),
            source_type=SourceType.MARKDOWN,
            size_bytes=-1,
        )
