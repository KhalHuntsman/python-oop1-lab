#!/usr/bin/env python3

"""
Author: Hunter Steele
Date: 12/5/25
Version: 1.1

Book Class:
- Represents a book with a title and a page count.
- The title is stored exactly as provided.
- The page_count attribute is validated using a property setter:
      * page_count must be an integer.
      * If a non-integer is assigned, the class prints:
            "page_count must be an integer"
        and stores None.
- Includes turn_page(), which prints a message simulating flipping a page.
"""

import math

class Book:
    def __init__(self, title, page_count):
        # Store the title exactly as provided
        self.title = title

        # Assign the page count through the property setter
        # This ensures validation occurs whenever page_count is set
        self.page_count = page_count

    @property
    def page_count(self):
        # Getter returns the internally stored page count
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Validate that page_count is an integer
        if isinstance(value, int):
            self._page_count = value  # Store valid integer
        else:
            # Print required error message if value is not an integer
            print("page_count must be an integer")

            # Store None to indicate invalid input was provided
            self._page_count = None

    def turn_page(self):
        # Method that simulates turning a page in the book
        print("Flipping the page...wow, you read fast!")
