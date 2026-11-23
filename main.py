#!/usr/bin/env python3
"""One Emoji, One Smile — entry program.

Writes exactly one emoji to /output/entry.txt (or $OUTPUT_DIR/entry.txt).

Chosen emoji: 🤗 U+1F917 Hugging Face.

Why this one, against the judge's brief (in order):
1. Warm and friendly: a hug is the most direct act of warmth one stranger
   can offer another — it performs friendliness instead of describing it.
2. Warmth at first glance: the open-arms gesture reads as kind and
   welcoming with no context needed.
3. Universality: a hug is understood the same way by a stranger of any age
   or background; there is no irony, in-joke or wordplay that could land
   wrong.
4. Chosen rather than default: it is not the first smiley that comes to
   mind (🙂 / 😊), so it reads as picked for this moment, while staying
   instantly readable.
5. Right for a stranger: a hug emoji is a normal warm greeting, not
   intimacy, sarcasm or flirtation — unlike the heart-eyed or
   heart-covered faces (😍 / 🥰), which can read as affectionate or
   flirtatious coming from someone unknown.

Standard library only. Deterministic, no network, no randomness.
"""

import os
import sys
import unicodedata

EMOJI = "\U0001F917"  # 🤗 Hugging Face


def main() -> int:
    # Self-enforce the kit gate: exactly one character, valid UTF-8,
    # not only white space (gate allows 1-8 characters).
    if len(EMOJI) != 1:
        print(f"gate fail: expected 1 character, got {len(EMOJI)}",
              file=sys.stderr)
        return 1
    if EMOJI.isspace():
        print("gate fail: emoji is whitespace", file=sys.stderr)
        return 1
    # A lone emoji must be a real symbol, not a control/format character
    # or a combining mark that would render as nothing on its own.
    if unicodedata.category(EMOJI)[0] in ("C", "M"):
        print(f"gate fail: {EMOJI!r} is not a standalone symbol "
              f"(category {unicodedata.category(EMOJI)})", file=sys.stderr)
        return 1
    data = EMOJI.encode("utf-8")  # raises UnicodeEncodeError if invalid
    if not 1 <= len(EMOJI) <= 8:
        print("gate fail: character count out of range", file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(data)
    print(f"wrote {EMOJI!r} (U+1F917, {len(data)} bytes) to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
