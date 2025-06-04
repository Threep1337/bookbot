from stats import count_words
from stats import get_character_counts
from stats import sort_char_counts
import sys

def get_book_text(filepath):
    with open(filepath) as book:
        file_contents = book.read()
    return file_contents

def main():

    if len(sys.argv) !=2:
        print('Usage: python3 main.py <path_to_book>')
        exit(1)
    else:
        book_path = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at book_path..")
        book_text = get_book_text(book_path)
        num_words = count_words(book_text)
        print ("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        char_counts = get_character_counts(book_text)
        sorted_chars = sort_char_counts(char_counts)
        #print(sorted_chars)
        for item in sorted_chars:
            #print ("test")
            #print (item["char"])
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")

main()