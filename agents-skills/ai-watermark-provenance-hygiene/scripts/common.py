from __future__ import annotations

import pathlib

TEXT_EXTS = {".txt", ".md", ".markdown", ".html", ".htm", ".json", ".csv", ".xml", ".yaml", ".yml"}
IMAGE_EXTS = {".png", ".jpg", ".jpeg"}


def read_text(path: str) -> str:
    return pathlib.Path(path).read_text(encoding="utf-8")


def write_text(path: str, text: str) -> None:
    pathlib.Path(path).write_text(text, encoding="utf-8")
