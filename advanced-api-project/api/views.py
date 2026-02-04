# After — recommended style using generics.ListAPIView
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Enable the three filter backends
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Step 1: Filtering (exact match by default, e.g. ?title=... &author=... &publication_year=...)
    filterset_fields = [
        'title',
        'author',
        'publication_year',
        # Add more fields if you have them, e.g. 'genre', 'isbn'
    ]

    # Step 2: Search (partial, case-insensitive match on title or author)
    # Example: ?search=python  → matches "Python Crash Course" or author "Eric Matthes"
    search_fields = [
        'title',
        'author',
        # You can add '^title' for startswith, '=title' for icontains exact, etc.
        # Default is icontains (partial match)
    ]

    # Step 3: Ordering
    # Example: ?ordering=title          → ascending by title
    #          ?ordering=-publication_year → newest first
    ordering_fields = [
        'title',
        'publication_year',
        'author',
        # Add more if needed
    ]

    # Optional: default ordering if no ?ordering= param is provided
    ordering = ['title']  # or ['-publication_year'] for newest first