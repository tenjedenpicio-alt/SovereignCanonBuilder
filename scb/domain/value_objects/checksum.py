from __future__ import annotations

import re
from dataclasses import dataclass

_SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True, slots=True)
class Checksum:
    """
    Immutable SHA-256 checksum.

    A Checksum represents the SHA-256 digest of a source document.
    """

    value: str

    def __post_init__(self) -> None:
        if self.value != self.value.strip():
            raise ValueError(
                "Checksum must not contain leading or trailing whitespace."
            )

        if not _SHA256_PATTERN.fullmatch(self.value):
            raise ValueError(
                "Checksum must be exactly 64 lowercase hexadecimal characters."
            )

    def __str__(self) -> str:
        return self.value
