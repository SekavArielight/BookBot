def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def main():
    text_output = get_book_text("books/frankenstein.txt")
    print(text_output)


main()
