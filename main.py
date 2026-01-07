def get_book_text(filepath):
    with open(filepath) as f:
        file_text = f.read()
        return file_text

def main():
   text = get_book_text("books/frankenstein.txt")
   words = text.split()
   num_words = len(words)
   total = f"Found {num_words} total words"
   print(total)

main()
