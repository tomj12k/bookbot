def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def get_number_of_words(text):
    words = text.split()
    return len(words)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_number_of_words(book_text)
    print(f"Found {num_words} total words")
    #print(book_text[:])

main()