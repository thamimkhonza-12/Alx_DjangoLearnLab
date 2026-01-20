# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    for book in books:
        print(book.title)


# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(book.title)


# 3. Retrieve the librarian for a library
def librarian_of_library(library_name):
    librarian = Librarian.objects.get(library=Library.objects.get(name=library_name))
    print(librarian.name)

