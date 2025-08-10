from django.db import models

# Create your models here.
class Author(models.Model):
     """
    Represents a book author.

    Fields:
        name (CharField): The author's name.
    Relationships:
        One-to-Many with Book: An Author can have many Books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
     """
    Represents a book.

    Fields:
        title (CharField): Title of the book.
        publication_year (IntegerField): Year the book was published.
        author (ForeignKey): Link to the Author model.
    Relationships:
        Belongs to an Author (many books can belong to one author).
        Reverse lookup via 'books' related_name from Author.
    """
    title = models.CharField(max_length=255) 
    publication_year = models.IntegerField()  
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE, 
        related_name='books'      
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})" 



