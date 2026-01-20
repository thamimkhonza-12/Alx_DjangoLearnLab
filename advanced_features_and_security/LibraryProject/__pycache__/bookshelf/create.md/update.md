## 3. Update
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
updated_book = Book.objects.get(id=book.id)
print(updated_book)
# Expected output: Nineteen Eighty-Four by George Orwell (1949)