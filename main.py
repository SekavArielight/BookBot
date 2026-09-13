from stats import character_count, chars_dict_to_sorted_list, word_count


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        return f.read()


def print_report(book_path, word_count, sorted_list_char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char, count in sorted_list_char_count:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")

    print("============= END ===============")


def main() -> None:
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    characters_sorted_list = chars_dict_to_sorted_list(character_count(text))
    # print(f"Found {num_words} total words")
    # print(characters_sorted_list)
    print_report(book_path, num_words, characters_sorted_list)


main()
