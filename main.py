from stats import get_book_word_count, get_book_character_count, get_sorted_character_dictionary
import sys

def get_book_text(path):
    book_text = ""
    with open(path) as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    wc_txt = f"Found {get_book_word_count(book_path)} total words"
    character_count_string = ""
    char_list = get_sorted_character_dictionary(get_book_character_count(book_path))    
    for i in range(0, len(char_list)):
        character_count_string += f"{char_list[i]['char']}: {char_list[i]['count']}"
        if i < len(char_list) - 1:
            character_count_string += "\n"
    report_text = f"============ BOOKBOT ============\n" \
    f"Analyzing book found at {book_path}\n" \
    f"----------- Word Count ----------\n" \
    f"{wc_txt}\n" \
    f"--------- Character Count -------\n" \
    f"{character_count_string}\n" \
    f"============= END ==============="
    print(report_text)
    return None

main()