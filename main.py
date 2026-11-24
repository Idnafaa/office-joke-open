#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open.

Writes one original one-line office joke (at most 200 characters)
to /output/entry.txt. Standard library only.
"""

JOKE = (
    "The meeting that could have been an email just scheduled "
    "a follow-up meeting to discuss why it wasn't an email."
)


def write_entry(path="/output/entry.txt"):
    line = " ".join(JOKE.split())
    if not 1 <= len(line) <= 200:
        raise ValueError(f"joke must be 1-200 chars, got {len(line)}")
    if "\n" in line:
        raise ValueError("joke must be a single line")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    return line


if __name__ == "__main__":
    written = write_entry()
    print(f"wrote {len(written)} chars to /output/entry.txt")
