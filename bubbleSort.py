def BubbleSort(array):

    length = len(array)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def BubbleSortRecur(array, end):
    
    if end == 0:
        return
    for i in range(end - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    BubbleSortRecur(array, end - 1)

array = [8, 3, 1, 2, 5, 7, 6, 4, 7, 1, 89, 78, 21]
BubbleSortRecur(array, len(array))
print(array)