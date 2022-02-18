import sys

from pysa import IntArray

array = IntArray(10)
builtin_list = [100, 200, 300, 400, 500]

for element in builtin_list:
    array.append(element)

print(f"""
IntArray: {array}
IntArray memory usage: {array.get_size()}

Built-in list: {builtin_list}
Built-in list memory usage: {sys.getsizeof(builtin_list)}
""")

print(array[4])
