from django.contrib import admin

from .models import Book

from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters on the right-hand side
    list_filter = ('publication_year', 'author')

    # Enable search functionality
    search_fields = ('title', 'author')

