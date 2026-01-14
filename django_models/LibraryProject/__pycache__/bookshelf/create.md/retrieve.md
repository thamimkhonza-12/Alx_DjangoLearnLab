## 2. Retrieve
retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book)
# Expected output: 1984 by George Orwell (1949)
