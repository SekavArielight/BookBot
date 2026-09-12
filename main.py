from stats import word_count


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

text_output = get_book_text("books/frankenstein.txt")

def main():
    num_words = word_count("books/frankenstein.txt")
    print(f"Found {num_words} total words")


main()
