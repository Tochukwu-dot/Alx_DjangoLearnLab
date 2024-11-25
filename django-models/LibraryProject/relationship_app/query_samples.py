from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        print(f"No author found with name: {author_name}")
        return []

# List all books in a library
def query_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")
        return []

# Retrieve the librarian for a library
def query_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian found for library: {library_name}")
        return None

# Example usage
if __name__ == "__main__":
    # Query books by author
    author_name = "J.K. Rowling"
    books_by_author = query_books_by_author(author_name)
    print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

    # Query books in a library
    library_name = "Central Library"
    books_in_library = query_books_in_library(library_name)
    print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

    # Query librarian for a library
    librarian = query_librarian_for_library(library_name)
    if librarian:
        print(f"Librarian for {library_name}: {librarian.name}")
