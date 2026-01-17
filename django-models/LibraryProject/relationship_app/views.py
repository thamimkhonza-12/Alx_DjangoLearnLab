from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view (already implemented)
def book_list(request):
    books = Book.objects.select_related('author').all()
    output = [f"{book.title} by {book.author.name}" for book in books]
    return HttpResponse("<br>".join(output))


# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    context_object_name = "library"

    def render_to_response(self, context, **response_kwargs):
        library = context["library"]
        books = library.books.select_related("author").all()

        output = [f"Library: {library.name}", ""]
        for book in books:
            output.append(f"{book.title} by {book.author.name}")

        return HttpResponse("<br>".join(output))


from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Function-based view to list all books
def book_list_view(request):
    books = Book.objects.all()  # Query all books
    # Create a simple text output
    output = "<h2>List of Books</h2><ul>"
    for book in books:
        output += f"<li>{book.title} by {book.author.name}</li>"
    output += "</ul>"
    return HttpResponse(output)

from django.views.generic import DetailView
from .models import Library

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # We'll create this template
    context_object_name = "library"  # The object in the template

    # Add related books to the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # ManyToMany: all books in this library
        return context
