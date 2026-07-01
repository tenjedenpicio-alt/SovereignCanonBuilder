import pytest

from scb.domain.identifiers.document_id import DocumentId


def test_valid_document_id() -> None:
    doc_id = DocumentId("hogwarts_001")

    assert str(doc_id) == "hogwarts_001"


def test_document_ids_compare_equal() -> None:
    assert DocumentId("abc") == DocumentId("abc")


def test_document_ids_compare_not_equal() -> None:
    assert DocumentId("abc") != DocumentId("xyz")


@pytest.mark.parametrize(
    "value",
    [
        "",
        " ",
        " abc",
        "abc ",
        "abc/def",
        "abc\\def",
        "abc:def",
        "abc*",
    ],
)
def test_invalid_document_ids(value: str) -> None:
    with pytest.raises(ValueError):
        DocumentId(value)
