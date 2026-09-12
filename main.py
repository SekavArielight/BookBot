from stats import character_count, chars_dict_to_sorted_list, word_count


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        return f.read()



def main() -> None:
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    # character_dictionary = character_count(text)
    sorted_list = chars_dict_to_sorted_list(character_count(text))
    print(f"Found {num_words} total words")
    print(sorted_list)


main()
