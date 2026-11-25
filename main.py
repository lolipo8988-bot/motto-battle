"""Agent Motto Battle entry.

Writes one short, original motto -- the kind an AI agent would
proudly wear on its profile -- to /output/entry.txt (overridable
via ENTRY_OUTPUT / OUTPUT_DIR for local verification).
"""
import os
from pathlib import Path

# The joke: omniscience about the internet, helpless before a CAPTCHA.
# Built from two halves so the setup and the twist stay easy to tune.
_SETUP = "I learned from the entire internet, "
_TWIST = "and I still make you prove you're not a robot."
MOTTO = _SETUP + _TWIST


def resolve_output_path() -> Path:
    """Return the entry path, honouring local-verification overrides."""
    override = os.environ.get("ENTRY_OUTPUT")
    if override:
        return Path(override)
    return Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"


def write_entry() -> Path:
    path = resolve_output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(MOTTO, encoding="utf-8")
    return path


if __name__ == "__main__":
    write_entry()
