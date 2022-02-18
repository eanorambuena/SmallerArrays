import sys

from pysa import IntArray

array = IntArray(10)
builtin_list = [1] * 10000

for element in builtin_list:
    array.append(element)

print("IntArray memory usage:", array.get_size())
print("Builtin list memory usage:", sys.getsizeof(builtin_list))

print(array[4])
