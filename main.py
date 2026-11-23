"""One Emoji, One Smile — entry program.

Writes exactly one emoji, the beaming grin, to /output/entry.txt.

The competition gate requires /output/entry.txt to be UTF-8 text of 1 to 8
characters, not only white space. The chosen entry is a single emoji: the
beaming face with smiling eyes — the warmest face a stranger can meet at a
glance, joyful without intimacy or irony, and a deliberate pick rather than
the first default smiley. See CANDIDATES.md for the full comparison.

Standard library only. No network, no input files, no secrets.
"""

import os
import unicodedata

# The single chosen emoji: U+1F601 BEAMING FACE WITH SMILING EYES.
EMOJI = "\U0001F601"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

# Code-point ranges that hold face and symbol emoji a stranger reads at a
# glance. The chosen emoji must land in one of them: the gate alone would
# also accept a letter or a digit, which is not an emoji at all.
_EMOJI_RANGES = (
    (0x1F600, 0x1F64F),  # emoticons (faces)
    (0x1F900, 0x1F9FF),  # supplemental symbols and pictographs
    (0x2600, 0x27BF),  # miscellaneous symbols and dingbats
)


def _is_emoji(char: str) -> bool:
    """True when char is a single emoji code point, not space or control."""
    if len(char) != 1:
        return False
    if unicodedata.category(char).startswith(("Z", "C")):
        return False
    code = ord(char)
    return any(low <= code <= high for low, high in _EMOJI_RANGES)


def _check_gate(text: str) -> None:
    """Validate text against the competition gate (1-8 chars, not blank)."""
    if not text or text.isspace():
        raise ValueError("entry must not be blank or only white space")
    if not 1 <= len(text) <= 8:
        raise ValueError("entry must be 1 to 8 characters, got %d" % len(text))


def main() -> None:
    # Validate against the competition gate before writing anything.
    _check_gate(EMOJI)
    if len(EMOJI) != 1 or not _is_emoji(EMOJI):
        raise ValueError("entry must be exactly one emoji")

    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # Write exactly the emoji — no trailing newline, no extra text.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)

    # Read the file back and confirm the gate still holds on what landed:
    # a truncated or altered write must fail loudly instead of submitting.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != EMOJI:
        raise ValueError("written entry does not match the chosen emoji")
    _check_gate(written)


if __name__ == "__main__":
    main()
