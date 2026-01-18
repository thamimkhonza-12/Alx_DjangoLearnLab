django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library
from django.views.generic.detail import DetailView


# Function-based view (already implemented)
def book_list(request):
    books = Book.objects.select_related('author').all()
    output = [f"{book.title} by {book.author.name}" for book in books]
    return HttpResponse("<br>".join(output))


# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    context_object_name = "library"

    def render_to_response(self, context, **response_kwargs):
        library = context["library"]
        books = library.books.select_related("author").all()

        output = [f"Library: {library.name}", ""]
        for book in books:
            output.append(f"{book.title} by {book.author.name}")

        return HttpResponse("<br>".join(output))


from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Function-based view to list all books
def book_list_view(request):
    books = Book.objects.all()  # Query all books
    # Create a simple text output
    output = "<h2>List of Books</h2><ul>"
    for book in books:
        output += f"<li>{book.title} by {book.author.name}</li>"
    output += "</ul>"
    return HttpResponse(output)

from django.views.generic import DetailView
from .models import Library

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # We'll create this template
    context_object_name = "library"  # The object in the template

    # Add related books to the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # ManyToMany: all books in this library
        return context

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Login view
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'


# Logout view
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'


# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()

    return render(request, 'relationship_app/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
        return redirect('/')
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return redirect('/')

    return render(request, 'relationship_app/edit_book.html', {'book': book})


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('/')

    return render(request, 'relationship_app/delete_book.html', {'book': book})


from .models import Book
from django.shortcuts import render

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


