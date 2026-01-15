from django_models.relationship_app.models import Library
from relationship_app.models import Author, library # type: ignore



# ---------------------------------------
# Query 1: Get all books by a given author
# ---------------------------------------
def get_books_by_author(author_name):
    """
    Returns all books written by the given author.
    """
    author = Author.objects.filter(name=author_name).first()
    if author:
        return author.books.all()
    return []


# ---------------------------------------
# Query 2: Get all books in a library
# ---------------------------------------
def get_books_in_library(library_name):
    """
    Returns all books available in the given library.
    """
    library = Library.objects.filter(name=library_name).first()
    if library:
        return library.books.all()
    return []


# ---------------------------------------
# Query 3: Get librarian for a library
# ---------------------------------------
def get_librarian_for_library(library_name):
    """
    Returns the librarian responsible for the given library.
    """
    library = Library.objects.filter(name=library_name).first()
    if library and hasattr(library, "librarian"):
        return library.librarian
    return None
