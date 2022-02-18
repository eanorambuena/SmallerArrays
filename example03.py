import sys
from pysa import String

builtin_string = "Supercalifragilisticexpialidocious"
string = String(builtin_string)

print(f"""
String: '{string}'
String memory usage: {string.size}

Built-in string: '{builtin_string}'
Built-in string memory usage: {sys.getsizeof(builtin_string)}
""")
