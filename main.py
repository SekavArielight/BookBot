from stats import word_count


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        return f.read()



def main() -> None:
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    print(f"Found {num_words} total words")


main()
