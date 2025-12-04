import json
import logging
from pathlib import Path
from .book import Book

logger = logging.getLogger(__name__)

class LibraryInventory:

    def __init__(self, json_path="books.json"):
        self.json_path = Path(json_path)
        self.books = []
        self.load()

    def load(self):
        if not self.json_path.exists():
            logger.info("No JSON found. Creating new inventory.")
            self.books = []
            return

        try:
            with open(self.json_path, "r") as f:
                data = json.load(f)
            self.books = [Book(**item) for item in data]
        except Exception as e:
            logger.error("Error loading JSON:", e)
            self.books = []

    def save(self):
        try:
            with open(self.json_path, "w") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=2)
        except Exception as e:
            logger.error("Error saving JSON:", e)

    def add_book(self, title, author, isbn):
        if self.search_by_isbn(isbn):
            raise ValueError("ISBN already exists!")

        book = Book(title, author, isbn)
        self.books.append(book)
        self.save()
        return book

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        return self.books

    def issue_book(self, isbn):
        b = self.search_by_isbn(isbn)
        if not b:
            raise ValueError("Book not found")
        if not b.issue():
            raise ValueError("Book already issued")
        self.save()

    def return_book(self, isbn):
        b = self.search_by_isbn(isbn)
        if not b:
            raise ValueError("Book not found")
        if not b.return_book():
            raise ValueError("Book is not issued")
        self.save()
