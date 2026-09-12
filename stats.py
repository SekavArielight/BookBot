# Write a new function that accepts the book's text as a string and returns its word count as an integer.
def word_count(text: str) -> int:
    split_words = text.split()
    return len(split_words)


def character_count(text: str) -> dict[str, int]:
    characters = {}

    for char in text:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters
