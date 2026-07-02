from pathlib import Path

from scb.compiler.stages.loader import discover_documents


def test_discover_documents(tmp_path: Path) -> None:
    """
    The loader should discover every supported lore document.
    """

    (tmp_path / "Lore.md").write_text("# Lore")
    (tmp_path / "History.txt").write_text("History")
    (tmp_path / "Notes.odt").write_text("Notes")

    ignored = tmp_path / "ignore.pdf"
    ignored.write_text("ignore me")

    documents = discover_documents(tmp_path)

    assert len(documents) == 3

    names = {doc.relative_path.name for doc in documents}

    assert names == {
        "Lore.md",
        "History.txt",
        "Notes.odt",
    }
