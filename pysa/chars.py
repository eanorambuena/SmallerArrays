from pysa.numbers import IntArray
from pysa.utils import binary_list_to_string

DEFAULT_CHAR_BINARY_SIZE  = 8
DEFAULT_CHAR_DECIMAL_SIZE = 3 # int(log(2 ** DEFAULT_CHAR_BINARY_SIZE, 10))
class CharArray(IntArray):

    def __init__(self, string = None, items_size = DEFAULT_CHAR_BINARY_SIZE, auto_resize = False):
        super().__init__(string, items_size, auto_resize)

    def append(self, element):
        str_element = str(element)
        bin_element = "".join(format(ord(c), 'b') for c in str_element)
        super().append(int(bin_element))

    def to_string(self):
        return binary_list_to_string(self)

class String(CharArray):
    
    def __init__(self, string = None, items_size = DEFAULT_CHAR_BINARY_SIZE, auto_resize = False):
        super().__init__(string, items_size, auto_resize)

    def __str__(self):
        return self.to_string()
