from stats import get_num_words
def get_book_text(ruta):
    with open(ruta) as f:
        file_contents = f.read()
    return file_contents

def main():
    works = get_book_text("./books/frankenstein.txt")
    get_num_words(works)
main()