import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Book, Author, Library, Librarian


# 1. Query all books by a specific author
author_name = "Chinua Achebe"
author = Author.objects.get(name=author_name)  
books_by_author = Book.objects.filter(author=author) 

# 2. List all books in a library
library_name = "Main City Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

# 3. Retrieve the librarian for a library (Must use this exact query)
librarian = Librarian.objects.get(library=library) 
