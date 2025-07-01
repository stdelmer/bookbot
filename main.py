def get_book_text(ruta):
    with open(ruta) as f:
        file_contents = f.read()
    return file_contents
def book_return(works):
    num_work = works.split()
    num_works = len(num_work)
    print(f"{num_works} words found in the document")
    return num_works
def main():
    works = get_book_text("./books/frankenstein.txt")
    book_return(works)
main()