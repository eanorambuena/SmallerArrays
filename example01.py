import sys

from pysa import IntArray

builtin_list = [100, 200, 300, 400, 500]
array = IntArray(builtin_list)

print(f"""
IntArray: {array}
IntArray memory usage: {array.size}

Built-in list: {builtin_list}
Built-in list memory usage: {sys.getsizeof(builtin_list)}
""")

print(array[4])
