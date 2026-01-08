def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    characters = {}
    text = text.lower()
    for t in text:
        if t in characters:
            characters[t] += 1
        else:
            characters[t] = 1
    return characters

def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    chars_list = []

    for char, count in num_chars_dict.items():
        char_dict = {"char": char, "num": count}
        chars_list.append(char_dict)
    
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
