import sys

from pysa import IntArray

a = IntArray(10)
b = [1] * 10000

for e in b:
    a.append(e)

print("IntArray memory usage:", a.get_size())
print("Builtin List memory usage:", sys.getsizeof(b))

print(a[4])