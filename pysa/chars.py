from pysa.numbers import IntArray
from pysa.utils import binary_to_string

class CharArray(IntArray):

    def __init__(self, string = None, items_size = 8, auto_resize = False):
        super().__init__(string, items_size, auto_resize)

    def append(self, element):
        str_element = str(element)
        bin_element = "".join(format(ord(c), 'b') for c in str_element)
        super().append(int(bin_element))

    def to_string(self):
        return binary_to_string(self)

class String(CharArray):
    
    def __init__(self, string = None, items_size = 8, auto_resize = False):
        super().__init__(string, items_size, auto_resize)

    def __str__(self):
        return self.to_string()
