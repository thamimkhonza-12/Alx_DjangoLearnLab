# bookshelf/admin.py
# This file integrates the Book model with the Django admin interface
# and customizes its display for better management and visibility.

from django.contrib import admin
from .models import Book  # Import the Book model from models.py

# Define a custom admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Book model.
    """
    # Columns to display in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Fields that can be searched in the admin search bar
    search_fields = ('title', 'author')
    
    # Sidebar filters for quick filtering by publication year
    list_filter = ('publication_year',)

# Register the Book model with the custom admin configuration
admin.site.register(Book, BookAdmin)




