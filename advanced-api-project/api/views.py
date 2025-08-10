from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import BookSerializer

# ---------------------------
# List all books
# ---------------------------
class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all Book instances.
    Allows read-only access to unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ---------------------------
# Retrieve a single book by ID
# ---------------------------
class BookList(generics.ListAPIView):
    """
    View for listing books with filtering, searching, and ordering enabled.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtering fields
    filterset_fields = ['title', 'author__name', 'publication_year']
    
    # Searchable fields
    search_fields = ['title', 'author__name']
    
    # Orderable fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering


# ---------------------------
# Create a new book
# ---------------------------
class BookCreateView(generics.CreateAPIView):
    """
    Creates a new Book instance.
    Only authenticated users can create.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ---------------------------
# Update an existing book
# ---------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing Book instance.
    Only authenticated users can update.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ---------------------------
# Delete a book
# ---------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a Book instance.
    Only authenticated users can delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
