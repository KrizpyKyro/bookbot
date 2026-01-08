import sys
from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        book_path = sys.argv[1]

    text = get_book_text(book_path)

    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    count_char = get_chars_dict(text)
    sorted_chars = chars_dict_to_sorted_list(count_char)
    
    for item in sorted_chars:
        char = item["char"]
        count = item["num"]

        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()
