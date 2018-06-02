def SelectSort(array):
    if len(array) <= 1:
        return

    length = len(array)
    for i in range(length):
        for j in range(i + 1, length):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

array = [8, 3, 1, 2, 5, 7, 6, 4, 7, 1, 89, 78, 21]
array = SelectSort(array)
print(array)
