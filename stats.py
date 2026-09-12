# Write a new function that accepts the book's text as a string and returns its word count as an integer.
def word_count(text: str) -> int:
    split_words = text.split()
    return len(split_words)
