import sys
from pysa import String

string = String()
builtin_string = "Supercalifragilisticexpialidocious"

for char in builtin_string:
    string.append(char)

print(f"""
String: '{string}'
String memory usage: {string.size}

Built-in string: '{builtin_string}'
Built-in string memory usage: {sys.getsizeof(builtin_string)}
""")
