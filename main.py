"""Have You Tried Turning It Off?

Writes one funny line to $MAKEFUN_OUTPUT_DIR/entry.txt: what a
hopeless tech support agent says to a desperate customer after
already turning it off and on again. Standard library only.
"""

import os
import sys

SUPPORT_LINE = (
    "I already turned it off and on again for you. "
    "It didn't work, but at least now we can both say we tried."
)


def support_line_check(text):
    """Check the support line against the competition gate.

    The gate wants plain UTF-8 text of 1 to 199 characters, not
    only white space, on a single line: one funny line a hopeless
    tech support agent says to a desperate customer. Returns the
    cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("support line must not be only whitespace")
    if len(cleaned) > 199:
        raise ValueError(
            "support line is %d characters, over the 199 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("support line must be exactly one line")
    return cleaned


def support_line_shape(text):
    """Measure the support line for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A line too short to carry a joke, or one
    padded out to fill the cap instead of landing the twist, is
    caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = support_line_check(SUPPORT_LINE)
    shape = support_line_shape(text)
    if shape["words"] < 5:
        raise ValueError("support line is too short to carry a joke")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
