
---

### 📄 `update.md`

```md
# Update Book Record

## Django Shell Command

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
