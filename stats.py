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


def sort_on(char_count: tuple[str, int]) -> int:
    return char_count[1]


def chars_dict_to_sorted_list(
    num_char_dict: dict[str, int],
) -> list[tuple[str, int]]:
    characters_list: list[tuple[str, int]] = []

    for char in num_char_dict:
        count = num_char_dict[char]
        characters_tuple = (char, count)
        characters_list.append(characters_tuple)

    sorted_characters_list = sorted(characters_list, reverse=True, key=sort_on)

    return sorted_characters_list
