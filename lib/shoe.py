#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size
        self._condition = "New"  # Initialize the condition attribute

    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if not isinstance(size, int):
            print ("size must be an integer")
        else:
            self._size = size

    size = property(get_size, set_size,)  

    def cobble(self):
        print ("Your shoe is as good as new!")  
        self._condition = "New"  # Set the condition to 'New' after repair

    def condition(self):
        return self._condition 
    
    condition = property(condition, cobble)