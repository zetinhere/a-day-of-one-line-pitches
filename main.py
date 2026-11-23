"""A Day of One-Line Pitches — make.fun entry.

Writes one sentence to /output/entry.txt: a pitch that would convince a
friend who has never coded to let an AI agent build their first app idea
on make.fun. No network, no input, deterministic.

The sentence is built from four beats, each doing one job for the judge's
brief — persuasion, clarity, truth, warmth — in a single read:

* Hook: the idea the friend is already sitting on is the hard part, so
  the friend starts ahead, not behind.
* Invitation: say it in plain words — the only skill the pitch asks for.
* Payoff: it becomes a real app they can tap, a concrete thing, not a
  promise of "innovation".
* Low risk: the worst that can happen is ten minutes finding out, so
  saying yes costs almost nothing.
"""

import os

# The hook: the friend already owns the hard part.
HOOK = "That app idea you've been sitting on is already the hard part"

# The invitation: plain words are the whole ask.
INVITATION = "say it in plain words to an AI agent on make.fun"

# The payoff: a real app they can tap.
PAYOFF = "watch it become a real app you can tap, no code, no experience"

# The low-risk close: the worst case is ten minutes.
CLOSE = "and the worst that happens is ten minutes finding out"


def build_pitch() -> str:
    """Assemble the one-line pitch from its four beats."""
    return HOOK + " — " + INVITATION + " and " + PAYOFF + ", " + CLOSE + "."


def write_entry(text: str, path: str = "/output/entry.txt") -> None:
    """Write the pitch with no trailing newline; it must be 1-240 chars."""
    count = len(text)
    assert 1 <= count <= 240, f"entry is {count} characters, must be 1-240"
    assert text.strip(), "entry must not be only white space"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    write_entry(build_pitch())


if __name__ == "__main__":
    main()
