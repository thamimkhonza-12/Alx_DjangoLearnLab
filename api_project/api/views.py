from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Book
from .serializers import BookSerializer


# ----------------------------
# READ-ONLY LIST VIEW
# ----------------------------
# Anyone can view the list of books (GET only)

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# ----------------------------
# FULL CRUD VIEWSET
# ----------------------------
# Handles Create, Read, Update, Delete
# Requires authentication via token

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Only authenticated users can access these endpoints
    permission_classes = [IsAuthenticated]