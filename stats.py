def num_of_words(book):
    book_list = book.split()
    return len(book_list)

def count_characters(book):
    characters = {}
    book = book.lower()
    for character in book:
        characters[character] = characters.get(character, 0) + 1
    return characters

def sort_on(char):
    return char["num"]

def build_rows(counts):
    rows = []
    for ch, n in counts.items():
        rows.append({"char": ch, "num": n})
    # now sort descending by "num"
    rows.sort(reverse=True, key=sort_on)
    return rows



