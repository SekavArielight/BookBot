def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def main():
    # text_output = get_book_text("books/frankenstein.txt")
    num_words = word_count("books/frankenstein.txt")
    print(f"Found {num_words} total words")


# Write a new function that accepts the book's text as a string and returns its word count as an integer.
def word_count(path_to_file):
    book_text = get_book_text(path_to_file)
    split_words = book_text.split()
    return len(split_words)


main()
