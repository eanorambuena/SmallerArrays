import sys
from pysa import CharArray

builtin_string = "Pizza"
array = CharArray(builtin_string)

print(f"""
CharArray: {array}
Decoded CharArray: '{array.to_string()}'
CharArray memory usage: {array.size}

Built-in string: '{builtin_string}'
Built-in string memory usage: {sys.getsizeof(builtin_string)}
""")
