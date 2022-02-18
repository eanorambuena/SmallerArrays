import sys
from pysa import CharArray

word = "Pizza"

a = CharArray(10)

for char in word:
    a.append(char)

print(f"""
SmallArray: {a}
Decoded SmallArray: '{a.to_string()}'
Size: {a.get_size()}

Built-in string: '{word}'
Built-in string size: {sys.getsizeof(word)}
""")
