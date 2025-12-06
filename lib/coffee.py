#!/usr/bin/env python3

"""
Author: Hunter Steele
Date: 12/5/25
Version: 1.1

Coffee Class:
- Represents a coffee order with a specific size and price.
- Valid sizes are exactly: "Small", "Medium", or "Large".
- When an invalid size is assigned, the class prints:
      "size must be Small, Medium, or Large"
- Includes a tip() method that:
      - Prints: "This coffee is great, here’s a tip!"
      - Adds $1.00 to the current coffee price.
"""

class Coffee:
    # Allowed sizes exactly as required by tests (case-sensitive)
    ALLOWED_SIZES = ["Small", "Medium", "Large"]

    def __init__(self, size, price):
        # Assign price as provided
        self.price = price

        # Assign size through property setter (ensures validation happens)
        self.size = size

    @property
    def size(self):
        # Getter returns the current stored size
        return self._size

    @size.setter
    def size(self, value):
        # Validate that size matches one of the allowed options
        if value in Coffee.ALLOWED_SIZES:
            self._size = value   # Store size exactly as given
        else:
            # Print required error message EXACTLY as tests expect
            print("size must be Small, Medium, or Large")
            self._size = None    # Store None when invalid size is provided

    def tip(self):
        # Print required message when tip is given
        print("This coffee is great, here’s a tip!")

        # Increase the price of the coffee by $1.00
        self.price = self.price + 1
