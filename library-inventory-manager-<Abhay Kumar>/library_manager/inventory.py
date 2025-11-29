# library_manager/inventory.py

import json
from pathlib import Path
from .book import Book


class LibraryInventory:
    def __init__(self, catalog_file="data/catalog.json"):
        self.catalog_file = Path(catalog_file)
        self.books = []
        self.load_catalog()

    def load_catalog(self):
        """Load books from JSON. If file missing or corrupted, create a new one."""
        try:
            if self.catalog_file.exists():
                with open(self.catalog_file, "r") as f:
                    data = json.load(f)
                    self.books = [Book(**b) for b in data]
            else:
                self.save_catalog()
        except Exception:
            # If any error happens, reset to empty list
            self.books = []
            self.save_catalog()

    def save_catalog(self):
        """Save current list of books to JSON."""
        with open(self.catalog_file, "w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_catalog()

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self):
        return self.books

    def issue_book(self, isbn):
        book = self.search_by_isbn(isbn)
        if book and book.is_available():
            book.issue()
            self.save_catalog()
            return True
        return False

    def return_book(self, isbn):
        book = self.search_by_isbn(isbn)
        if book and not book.is_available():
            book.return_book()
            self.save_catalog()
            return True
        return False
