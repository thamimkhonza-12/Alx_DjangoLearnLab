# Imports (only once at top)
from django.http import HttpResponse
from django.views.generic import DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from .models import Book, Library, Author, Librarian

# -------------------------
# Function-based view (already implemented)
# -------------------------
def book_list(request):
    books = Book.objects.select_related('author').all()
    output = [f"{book.title} by {book.author.name}" for book in books]
    return HttpResponse("<br>".join(output))

# -------------------------
# Class-based view
# -------------------------
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

# -------------------------
# Function-based view to list all books
# -------------------------
def book_list_view(request):
    books = Book.objects.all()  # Query all books
    output = "<h2>List of Books</h2><ul>"
    for book in books:
        output += f"<li>{book.title} by {book.author.name}</li>"
    output += "</ul>"
    return HttpResponse(output)

# -------------------------
# Class-based view for library details
# -------------------------
class LibraryDetailViewWithTemplate(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context

# -------------------------
# Authentication views
# -------------------------
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

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

# -------------------------
# Book CRUD views with permissions
# -------------------------
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

# -------------------------
# Function-based view to list all books (for templates)
# -------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# -------------------------
# Admin-only view (defined once)
# -------------------------
@user_passes_test(lambda u: u.is_staff)
def admin_view(request):
    return HttpResponse("Admin dashboard")
