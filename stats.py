def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_characters(text):
    characters = {}
    text = text.lower()
    for t in text:
        if t in characters:
            characters[t] = characters[t] + 1
        else:
            characters[t] = 1
    return characters

def sort_dict()
    