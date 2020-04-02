# 100 books contest by David Dolejší
# Run without parameters to print the catalog
# Enter a list of Book IDs (0-99) to view books
# separated by spaces, eg:   0 15 7 42

import urllib.request
import json
from collections import defaultdict
from itertools import count
from PIL import Image


def fetch_data(url):
    request = urllib.request.Request(url=url)
    with urllib.request.urlopen(request) as response:
        return json.load(response)


def make_catalog(library):
    book_id = count()
    cat = defaultdict(list)
    for book in library:
        *first_name, last_name = book['author'].split()
        author = last_name + (", " + " ".join(first_name)
                              if first_name else '')
        cat[author].append((next(book_id), book['title']))
    return cat


def show_book_info(book):
    title, author, pages, year, language, image_link = \
        [book.get(key) for key in ('title', 'author',
                                   'pages', 'year', 'language', 'imageLink')]
    print('\n' + '*' * (len(title)+4))
    print(f'* {title} *')
    print('*' * (len(title)+4))
    print(f'written by {author} in year {year}')
    print(f'{pages} pages, language: {language}\n')
    print(process_image(IMAGE_BASE_URL + image_link))


def process_image(url):
    ASCII = r'█▓▒░'
    request = urllib.request.Request(url=url)
    with urllib.request.urlopen(request) as response:
        with Image.open(response) as image:
            w, h = image.size
            width, height = 24, int(24 * h / w)
            grayscale = image.convert('L').resize((width, height)).getdata()
            low, high = min(grayscale), max(grayscale)
            normalized = (int(3.99 * (x-low) / (high-low)) for x in grayscale)
            return '\n'.join(
                ''.join(ASCII[next(normalized)]
                        for _ in range(width))
                for _ in range(height))


def show_catalog(catalog):
    for author, books in sorted(catalog.items()):
        print(f'{author}:')
        for book_id, title in books:
            print(f'{book_id:10} {title}')


BOOKS_URL = "https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json"
IMAGE_BASE_URL = "https://raw.githubusercontent.com/benoitvallon/100-best-books/master/static/"

if __name__ == '__main__':
    library = fetch_data(BOOKS_URL)
    catalog = make_catalog(library)
    command = input("Enter your choice of books from the list:\n")
    if command:
        for book in command.split():
            try:
                show_book_info(library[int(book)])
            except IndexError:
                print(f'\nThe book {book} does not exist, choose another.\n')
    else:
        print("No input, showing the full catalog.")
        show_catalog(catalog)
        print("Please enter the numbers of your choices, separated by space")
