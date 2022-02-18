import sys
from pysa import FloatArray
builtin_array = [1.1, 2.2, 3.3, 4.4, 5.5]
array = FloatArray(builtin_array)

print(f"""
FloatArray: {array}
FloatArray memory usage: {array.size}

Built-in array: '{builtin_array}'
Built-in array memory usage: {sys.getsizeof(builtin_array)}
""")
