from django.urls import path
from .views import (
    add_book, edit_book, delete_book,
    user_login, user_logout, register
)
urlpatterns = [
    path("add_book/", add_book, name="add_book"),
    path("edit_book/<int:book_id>/", edit_book, name="edit_book"),
    path("delete_book/<int:book_id>/", delete_book, name="delete_book"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", register, name="register"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('books/view/', views.view_books, name='view_books'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/edit/', views.edit_book, name='edit_book'),
    path('books/delete/', views.delete_book, name='delete_book'),
]
