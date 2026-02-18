from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all().order_by('-created_at')

    serializer_class = PostSerializer

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filter_backends = [filters.SearchFilter]

    search_fields = ['title', 'content']

    def perform_create(self, serializer):

        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all().order_by('-created_at')

    serializer_class = CommentSerializer

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):

        serializer.save(author=self.request.user)

from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get users the current user follows
        following_users = self.request.user.following.all()

        # Include current user posts too (optional but recommended)
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

        # Return posts ordered by newest first
        return Post.objects.filter(
            author__in=following_users
        ).order_by('-created_at')

class LikePostView(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):

        post = generics.get_object_or_404(Post, pk=pk)

        like, created = Like.objects.get_or_create(
            user=request.user,
            post=post
        )

        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )

            return Response(
                {"message": "Post liked"},
                status=status.HTTP_201_CREATED
            )

        return Response(
            {"message": "You already liked this post"},
            status=status.HTTP_400_BAD_REQUEST
        )

class UnlikePostView(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):

        post = generics.get_object_or_404(Post, pk=pk)

        try:
            like = Like.objects.get(
                user=request.user,
                post=post
            )

            like.delete()

            return Response(
                {"message": "Post unliked"},
                status=status.HTTP_200_OK
            )

        except Like.DoesNotExist:

            return Response(
                {"message": "You haven't liked this post"},
                status=status.HTTP_400_BAD_REQUEST
            )
