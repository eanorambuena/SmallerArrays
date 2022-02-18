import sys
from pysa import CharArray

array = CharArray(10)
builtin_string = "Pizza"

for char in builtin_string:
    array.append(char)

print(f"""
CharArray: {array}
Decoded CharArray: '{array.to_string()}'
CharArray memory usage: {array.size}

Built-in string: '{builtin_string}'
Built-in string memory usage: {sys.getsizeof(builtin_string)}
""")
