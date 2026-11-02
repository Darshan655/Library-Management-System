"""
Unit tests for Library Management System
"""

import unittest
from library import Library

class TestLibraryManagementSystem(unittest.TestCase):
    def setUp(self):
        self.lib = Library()
        self.lib.add_book(1, "The Hobbit", "J.R.R. Tolkien")
        self.lib.add_book(2, "Brave New World", "Aldous Huxley")

    def test_add_book(self):
        book = self.lib.add_book(3, "Fahrenheit 451", "Ray Bradbury")
        self.assertEqual(len(self.lib.list_books()), 3)
        self.assertEqual(book.title, "Fahrenheit 451")

    def test_borrow_and_return_book(self):
        # Borrow book
        self.assertTrue(self.lib.borrow_book(1))
        # Borrow already borrowed book
        self.assertFalse(self.lib.borrow_book(1))
        # Return book
        self.assertTrue(self.lib.return_book(1))
        # Return non-borrowed book
        self.assertFalse(self.lib.return_book(1))

if __name__ == "__main__":
    unittest.main()
