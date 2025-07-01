def get_book_text(ruta):
    with open(ruta) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    onlin = get_book_text("./books/frankenstein.txt")
    print(onlin)
main()