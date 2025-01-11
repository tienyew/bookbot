def read_file_contents(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def count_words(words):
    word_list = words.split()
    return len(word_list)

def count_chars(text):
    characters = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def main():
    file_path = "./books/frankenstein.txt"
    text = read_file_contents(file_path)
    print(f"--- Begin report of {file_path} ---")
    print(f"{count_words(text)} words found in the document")

    character_list = []
    character_dictionary = count_chars(text)


    for char in character_dictionary:
        character_list.append({"name": char, "num": character_dictionary[char]})


    character_list.sort(reverse=True, key=sort_on)

    for char in character_list:
        print(f"The '{char["name"]}' was found {char["num"]} times")
    
    print("--- End report ---")

main()
