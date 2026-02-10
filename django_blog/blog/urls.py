from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]

from django.urls import path
from . import views
from .views import (
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    # POSTS
    path('', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),

    # COMMENTS
    path(
        'posts/<int:post_id>/comments/new/',
        CommentCreateView.as_view(),
        name='comment-create'
    ),
    path(
        'comments/<int:pk>/edit/',
        CommentUpdateView.as_view(),
        name='comment-update'
    ),
    path(
        'comments/<int:pk>/delete/',
        CommentDeleteView.as_view(),
        name='comment-delete'
    ),
]
