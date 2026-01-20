from django.urls import path
from .views import list_books, LibraryDetailView

from django.urls import path
from django.contrib.auth import views
from django.contrib.auth.views import LoginView, LogoutView


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

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
]

path("register/", views.register, name="register"),
path(
    "login/",
    LoginView.as_view(template_name="relationship_app/login.html"),
    name="login",
),
path(
    "logout/",
    LogoutView.as_view(template_name="relationship_app/logout.html"),
    name="logout",
),
