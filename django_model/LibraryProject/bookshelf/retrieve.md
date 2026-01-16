
---

### 📄 `retrieve.md`

```md
# Retrieve Book Record

## Django Shell Command

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.id, book.title, book.author, book.publication_year
