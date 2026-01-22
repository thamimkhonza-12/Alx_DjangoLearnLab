"""
Permissions & Groups Setup:

Custom permissions (can_view, can_create, can_edit, can_delete) are defined
in the Book model using Django's Meta.permissions.

User access is controlled via Django Groups:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

Views are protected using Django's @permission_required decorator.
Unauthorized access results in a 403 Forbidden response.
"""



from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required


@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    return HttpResponse("You are allowed to VIEW books.")


@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return HttpResponse("You are allowed to CREATE books.")


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request):
    return HttpResponse("You are allowed to EDIT books.")


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request):
    return HttpResponse("You are allowed to DELETE books.")

from django.shortcuts import render
from .models import Book
from django.db.models import Q
from django import forms
from .forms import ExampleForm


# Secure form for user input
class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=True)

def search_books(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.none()

    if form.is_valid():
        q = form.cleaned_data['query']
        # ORM query prevents SQL injection
        books = Book.objects.filter(Q(title__icontains=q) | Q(author__icontains=q))

    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})

MIDDLEWARE = [
    ...
    'csp.middleware.CSPMiddleware',  # add this line if using django-csp
]
