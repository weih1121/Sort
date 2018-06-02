import math
import random

def RadixSort(array, radix=10):
    k = int(math.ceil(math.log(max(array), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(k):
        for j in array:
            bucket[int(j / (radix ** i) % radix)].append(j)
        del array[:]
        for z in bucket:
            array += z
            del z[:]
    return array

array = []
for i in range(50):
    array.append(random.randint(0, 200))
array = RadixSort(array)
print(array)