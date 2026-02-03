from django.db import models

class Author(models.Model):
    """
    Author model represents a writer.
    One Author can be associated with multiple Book objects
    (one-to-many relationship).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a book written by an Author.
    Each Book is linked to exactly one Author using a ForeignKey.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()

    # ForeignKey creates a one-to-many relationship:
    # one Author -> many Books
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
