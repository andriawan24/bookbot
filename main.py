from stats import count_words, count_characters, sort_characters
import sys

def get_book_text(filepath: str) -> str:
    result = ""
    with open(filepath) as f:
        result = f.read()
    return result

def generateReport(path, words_count, sorted_chars):
    print(
        f"""
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {words_count} total words
--------- Character Count -------
"""
    )

    for chars in sorted_chars:
        print(f"{chars['char']}: {chars['num']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    num_words = count_words(book_content)
    num_characters = count_characters(book_content)
    sorted_chars = sort_characters(num_characters)
    
    generateReport(book_path, num_words, sorted_chars)

main()