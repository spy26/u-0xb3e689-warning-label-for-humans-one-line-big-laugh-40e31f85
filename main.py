# Warning Label for Humans: One Line, Big Laugh
# Entry: one single-line safety warning label for human beings, at most
# 160 characters. Funny first, plausible second; the laugh lands in the
# last few words, in the wording and rhythm of a real printed label.
#
# Why this line: "Do not leave in direct sunlight" is verbatim label
# language, the burn-peel-complain escalation is instantly recognisable
# human behaviour, and the twist is that the human repeats the exact
# mistake next year. No caffeine, no "do not shake", no "five minutes
# away" — the field is saturated with all three (see VARIANTS.md).

ENTRY = (
    "WARNING: Do not leave in direct sunlight. This human burns, peels, "
    "complains, and books the same beach holiday next year."
)

# The gate is strict: /output/entry.txt must be UTF-8 text of 1 to 160
# characters, not only white space. Fail loudly here rather than shipping
# an entry the sealed scorer would refuse.
assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} characters, gate needs 1-160"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
