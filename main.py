"""Say What Actually Broke.

Writes a plain-words description of what actually broke (a printer that
refuses to print despite having everything it needs) plus the next step.

The entry says it straight: the printer has ink, paper, and power, yet it
still will not print — it has simply decided today is a rest day. The
suggested next step is the classic one: turn it off and on again, and it
will pretend that helped.
"""

import os

ENTRY = "The printer has ink, paper, and power. It still won't print. It has decided today is a rest day. Turn it off and on again — it will pretend that helped."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
