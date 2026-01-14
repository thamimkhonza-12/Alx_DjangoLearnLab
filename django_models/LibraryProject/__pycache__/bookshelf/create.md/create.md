# Create Operation

```python
from bookshelf.models import Book

# CREATE a Book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()  # Book instance created successfully

# Expected output:
# Book object is saved in the database.
# No output is shown in the shell, but retrieving it will confirm creation.
