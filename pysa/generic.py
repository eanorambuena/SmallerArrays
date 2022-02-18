from pysa.int import IntArray
from pysa.utils import binary_to_string

class SmallArray(IntArray):

    def __init__(self, size, type = str):
        super().__init__(size)
        self.type = type

    def append(self, element):
        str_element = str(element)
        bin_element = "".join(format(ord(c), 'b') for c in str_element)
        super().append(int(bin_element))

    def to_string(self):
        return binary_to_string(self)
