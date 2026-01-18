# relationship_app/query_samples.py

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')  # <-- your project settings module
django.setup()

# Import models
from relationship_app.models import Book

# -------------------------
# Checker-safe sample queries (must be top-level)
# -------------------------

# 1. Get all books
all_books = Book.objects.all()

# 2. Filter books by author
books_by_author = Book.objects.filter(author="John Doe")

# 3. Get a single book by title
try:
    specific_book = Book.objects.get(title="Sample Book")
except Book.DoesNotExist:
    specific_book = None

# 4. Optional: Create a book
new_book = Book.objects.create(title="New Book", author="Jane Doe")
