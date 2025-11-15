from stats import num_of_words
from stats import count_characters
from stats import build_rows
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def main():
    book = get_book_text(book_path)
    return book

main_book = main()

count = num_of_words(main_book)

final_count = count_characters(main_book)
rows = build_rows(final_count)

# headers
print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {count} total words")
print("--------- Character Count -------")

# loop
for row in rows:
    ch = row["char"]
    if not ch.isalpha():
        continue
    print(f"{ch}: {row['num']}")

# footer
print("============= END ===============")

