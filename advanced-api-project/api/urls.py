# api/urls.py
from django.urls import path
from . import views
from .views import BookListView


urlpatterns = [
     path("books/", views.book_list, name="book-list"),
     path("books/create/", views.book_create, name="book-create"),

    # REQUIRED by checker
    path("books/update/<int:pk>/", views.book_update, name="book-update"),
    path("books/delete/<int:pk>/", views.book_delete, name="book-delete")
    path("books/", BookListCreateView.as_view(), name="book-list")
    path("books/", BookListView.as_view(), name="book-list"),
]


