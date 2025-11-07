def get_book_word_count(path):
    word_count = 0
    with open(path) as f:
        words = f.read().split()
        word_count = len(words)
    return word_count

def get_book_character_count(path):
    char_dictionary = {}
    with open(path) as f:
        content = f.read().lower()
        for char in content:
            if char in char_dictionary:
                char_dictionary[char] += 1
            else:
                char_dictionary[char] = 1
    return char_dictionary

def get_sorted_character_dictionary(char_dictionary):
    sorted_character_list = []
    for char in char_dictionary:
        if char.isalpha():
            new_character = {}
            new_character["char"] = char
            new_character["count"] = char_dictionary[char]
            sorted_character_list.append(new_character)
    sorted_character_list.sort(key=sort_on, reverse=True)
    return sorted_character_list

def sort_on(items):
    return items["count"]