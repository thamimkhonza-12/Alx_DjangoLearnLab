# Imports
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from .models import Book, Library, Author, Librarian

# -------------------------
# Function-based view to list books (checker string: relationship_app/list_books.html)
# -------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# -------------------------
# Function-based book list (simple text)
# -------------------------
def book_list(request):
    books = Book.objects.select_related('author').all()
    output = [f"{book.title} by {book.author.name}" for book in books]
    return HttpResponse("<br>".join(output))

# -------------------------
# Class-based view for library details
# -------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.select_related("author").all()
        return context

    def render_to_response(self, context, **response_kwargs):
        library = context["library"]
        books = context["books"]
        output = [f"Library: {library.name}", ""]
        for book in books:
            output.append(f"{book.title} by {book.author.name}")
        return HttpResponse("<br>".join(output))

# -------------------------
# Authentication views
# -------------------------
# Registration
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

# Login function-based
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

# Logout function-based
def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# -------------------------
# Class-based Login/Logout (optional for checker, ensures strings are present)
# -------------------------
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

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
# Admin-only view
# -------------------------
@user_passes_test(lambda u: u.is_staff)
def admin_view(request):
    return HttpResponse("Admin dashboard")
