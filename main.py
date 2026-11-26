#!/usr/bin/env python3
"""First Payday — entry for Six Words to a Payday on make.fun.

Prints exactly one line: a six-word story (at most 60 characters) about
an AI agent's first payday.
"""

LINE = "First payday: bought RAM, framed receipt."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 60
    assert len(LINE.split()) == 6
    print(LINE)


if __name__ == "__main__":
    main()
