# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
books_by_author = Book.objects.filter(author__name="Author Name")

# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(book.title)


# 3. Retrieve the librarian for a library
librarian_of_library = Library.objects.get(name="Library Name").librarian
