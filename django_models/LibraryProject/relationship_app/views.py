from django.shortcuts import render

from django.http import HttpResponse
from .models import Book


def book_list_view(request):
    """
    Function-based view that lists all books and their authors.
    """
    books = Book.objects.select_related('author')

    output = []
    for book in books:
        output.append(f"{book.title} by {book.author.name}")

    return HttpResponse("<br>".join(output))


from django.views.generic.detail import DetailView
from .models import Library


class LibraryDetailView(DetailView):
    """
    Class-based view to display a specific library and its books.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Optional, we can create a template
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all books related to this library
        context['books'] = self.object.books.all()
        return context

