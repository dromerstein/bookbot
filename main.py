from stats import count_book_words,count_char,sort_chars_by_count
import sys

def usage():
    print("Usage: python3 main.py <path_to_book>")

def get_book_text(path):
    with open(path) as f:
        file_contents=f.read()
    return(file_contents)

def main():
    if len(sys.argv)!=2:
        usage()
        sys.exit(1)
    filepath=sys.argv[1]
    sort={}
    print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...\n----------- Word Count ----------")
    text=get_book_text(filepath)
    number=count_book_words(text)
    print(f"Found {number} total words\n--------- Character Count -------")
    chars=count_char(text)
    sort=sort_chars_by_count(chars)
    for k in sort:
        test=k["char"]
        if test.isalpha():
            print(f"{k['char']}: {k['count']}")

main()

