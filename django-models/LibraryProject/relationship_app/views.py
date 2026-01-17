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

