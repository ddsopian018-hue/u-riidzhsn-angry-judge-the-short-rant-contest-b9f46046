#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — writes one rant to entry.txt.

Pure standard library. The grader runs this with MAKEFUN_OUTPUT_DIR set
to a fresh empty folder; the program writes exactly one UTF-8 line there.
"""

import os

# The rant is 281 characters: inside the 1-400 gate, single line, no padding.
# The angle is the self-checkout turning on you: you do the scanning, the
# bagging and the apologising, the machine files the complaint, and the one
# human on duty acts like a surgeon for pressing a single button. The rant
# stays in the customer's voice throughout — no narrator, no moral, just
# the accusation landing on the wrong person, which is where the laugh is.
RANT = (
    "I scanned the rice. The machine scanned the rice. Then the machine "
    "screamed 'UNEXPECTED ITEM IN THE BAGGING AREA' at the rice, froze, "
    "and summoned a human who pressed ONE button and walked off like a "
    "surgeon. I did the job, the machine took the credit, and somehow "
    "I'm the suspect."
)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(RANT + "\n")


if __name__ == "__main__":
    main()
