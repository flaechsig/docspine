"""Reading YAML front matter.

All scalar values are read as text. YAML 1.1 would otherwise turn ``0.1`` into a float,
``2026-10-03`` into a date and ``NO`` into ``False``. Only an empty value stays ``None``.
"""

from __future__ import annotations

from typing import Optional, Tuple

from ._vendor import yaml


class _TextLoader(yaml.SafeLoader):
    pass


_TextLoader.yaml_implicit_resolvers = {}
for _first, _resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items():
    _kept = [(tag, regexp) for tag, regexp in _resolvers if tag == "tag:yaml.org,2002:null"]
    if _kept:
        _TextLoader.yaml_implicit_resolvers[_first] = _kept


class FrontMatterError(ValueError):
    pass


def split(text: str) -> Tuple[Optional[str], str]:
    """Return (front matter, body). Front matter is None if the file has none."""
    text = text.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 3)
    while end != -1:
        after = text[end + 4:end + 5]
        if after in ("", "\n"):
            return text[4:end + 1], text[end + 5:]
        end = text.find("\n---", end + 4)
    raise FrontMatterError("front matter is not closed with ---")


def parse(text: str) -> Tuple[Optional[dict], str]:
    """Return (front matter as dict, body)."""
    raw, body = split(text)
    if raw is None:
        return None, body
    try:
        data = yaml.load(raw, Loader=_TextLoader)
    except yaml.YAMLError as exc:
        raise FrontMatterError(f"front matter is not valid YAML: {exc}") from exc
    if data is None:
        data = {}
    if not isinstance(data, dict):
        raise FrontMatterError("front matter is not a mapping")
    return data, body
