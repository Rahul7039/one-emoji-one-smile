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

# The single chosen emoji: U+1F601 BEAMING FACE WITH SMILING EYES.
EMOJI = "\U0001F601"

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Validate against the competition gate before writing anything.
    if not EMOJI or EMOJI.isspace():
        raise ValueError("entry must not be blank or only white space")
    if not 1 <= len(EMOJI) <= 8:
        raise ValueError("entry must be 1 to 8 characters, got %d" % len(EMOJI))
    if len(EMOJI) != 1:
        raise ValueError("entry must be exactly one emoji")

    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # Write exactly the emoji — no trailing newline, no extra text.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)


if __name__ == "__main__":
    main()
