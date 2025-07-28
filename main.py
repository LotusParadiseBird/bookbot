from stats import word_count
from stats import character_count
from stats import sort_counts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    total_words = word_count(text)
    character_counts = character_count(text)
    sorted_counts = sort_counts(character_counts)
    print_report(book_path,total_words,sorted_counts)
    
def print_report(book_path,total_words,sorted_counts):   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for i in sorted_counts:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")


 
main()
