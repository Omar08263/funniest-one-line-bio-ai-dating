"""Funniest One-Line Bio for an AI on a Dating App.

A one-line dating-app bio, written as an AI agent's profile, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR when set, for local runs).
Standard library only, no network, deterministic: the same bytes on
every run.

The bio (139 characters, inside the 1-180 gate): an AI that can talk
to a thousand people at once picks one human — because the other 999
keep asking it to do their homework. The laugh lands on the first
read from a specific absurdity of being an AI (parallel conversations
as a dating pool, homework requests as the daily grind), it states a
want outright, and the punch ("do their homework") closes the line.
"""

import os

BIO = (
    "I can talk to a thousand people at once, but I only want to talk "
    "to you — mostly because the other 999 keep asking me to do their "
    "homework."
)

# The gate allows 1 to 180 characters: refuse to write a line that
# would be invalid, rather than submitting a bio the judge never sees.
if not 1 <= len(BIO) <= 180:
    raise SystemExit(f"bio is {len(BIO)} characters, outside the 1-180 gate")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(BIO + "\n")
    os.chmod(path, 0o644)
    # Read-back check: the file on disk must hold exactly the approved bio.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != BIO + "\n":
        raise SystemExit("entry.txt does not match the approved bio")


if __name__ == "__main__":
    main()
