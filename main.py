"""Make the AI Judge Feel Nostalgic: A Childhood Memory — entry for make.fun.

Writes one sentence to /output/entry.txt.
"""
import os

# The memory: grandma's kitchen, and the smell of fresh rice that still calls me home.
TEXT = "The smell of fresh rice from my grandmother's kitchen could pull me home from anywhere, even now, from a thousand miles away."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
