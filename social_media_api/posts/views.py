from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


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
        following_users = list(following_users) + [self.request.user]

        # Return posts ordered by newest first
        return Post.objects.filter(
            author__in=following_users
        ).order_by('-created_at')
