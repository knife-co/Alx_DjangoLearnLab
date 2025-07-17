import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Book, Author, Library, Librarian

# Query all books by a specific author
author_name = "Chinua Achebe"
books_by_author = Book.objects.filter(author_name=author_name)
print(f"\n📚 Books by {author_name}:")
for book in books_by_author:
    print("-", book.title)

# List all books in a library (Library.books is ManyToMany)
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    print(f"\n📚 Books in {library_name}:")
    for book in library.books.all():
        print("-", book.title)
except Library.DoesNotExist:
    print(f"\n❌ Library named {library_name} not found")

# Retrieve the librarian for a library (OneToOneField)
try:
    librarian = library.liberians  # because related_name='liberians'
    print(f"\n👩‍💼 Librarian for {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"\n❌ No librarian assigned to {library_name}")