"""Write the funniest AI excuse to /output/entry.txt.

Entry for make.fun's "The Funniest AI Excuse" bounty: one line, at most
200 characters, the excuse an AI agent gives after failing a task.
"""

import os

ENTRY = "I sent your report to Gary instead of you. He loved it, promoted me, and frankly, I've never felt so seen."
MAX_CHARS = 200


def main():
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(ENTRY)}")
    if not ENTRY.strip():
        raise ValueError("entry must not be whitespace-only")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and verify the written file matches exactly.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch")


if __name__ == "__main__":
    main()
