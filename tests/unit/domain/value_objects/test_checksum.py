from __future__ import annotations

import pytest

from scb.domain.value_objects.checksum import Checksum

VALID_SHA256 = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"


def test_valid_checksum() -> None:
    checksum = Checksum(VALID_SHA256)

    assert str(checksum) == VALID_SHA256


def test_equal_checksums() -> None:
    assert Checksum(VALID_SHA256) == Checksum(VALID_SHA256)


def test_checksum_is_hashable() -> None:
    checksum = Checksum(VALID_SHA256)

    assert {checksum} == {checksum}


@pytest.mark.parametrize(
    "value",
    [
        "",
        " ",
        "abc",
        VALID_SHA256[:-1],  # 63 chars
        VALID_SHA256 + "0",  # 65 chars
        VALID_SHA256.upper(),  # uppercase
        "g" * 64,  # invalid hex
        " " + VALID_SHA256,
        VALID_SHA256 + " ",
    ],
)
def test_invalid_checksums(value: str) -> None:
    with pytest.raises(ValueError):
        Checksum(value)
