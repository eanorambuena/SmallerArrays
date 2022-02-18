import string
from pysa.int import IntArray

class SmallArray(IntArray):

    def __init__(self, size, type = string):
        super().__init__(size)
        self.type = type

    def append(self, element):
        str_element = str(element)
        bin_element = "".join(format(ord(c), 'b') for c in str_element)
        super().append(int(bin_element))
