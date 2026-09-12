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


def sort_on(text_tuple: tuple[str, int]) -> int:
    return text_tuple[1]


def chars_dict_to_sorted_list(characters_dictionary: dict[str, int]) -> list[tuple[str, int]]:
    characters_list = []

    for char in characters_dictionary:
        dictionary_count = characters_dictionary[char]
        characters_tuple = (char, dictionary_count)
        characters_list.append(characters_tuple)
        
    sorted_characters_list = sorted(characters_list, reverse=True, key=sort_on)

    return sorted_characters_list
