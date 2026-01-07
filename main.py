from stats import get_num_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    count_char = count_characters(text)
    print(count_char)

main()
