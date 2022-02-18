from pysa import SmallArray, binary_to_ascii
from pysa.utils import binary_to_string
import sys

a = SmallArray(10)
word = "Pizza"

for ch in word:
    a.append(ch)

print(f"""
SmallArray: {a}
Decoded SmallArray: '{binary_to_string(a)}'
Size: {a.get_size()}

Built-in string: '{word}'
Built-in string size: {sys.getsizeof(word)}
""")
