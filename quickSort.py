def QuickSortRecur(array, start, end):
    if start >= end:
        return
    low, high, pivotKey = start, end, array[start]
    while low < high:
        while low < high and array[high] >= pivotKey:
            high -= 1
        array[low], array[high] = array[high], array[low]
        while low < high and array[low] <= pivotKey:
            low += 1
        array[low], array[high] = array[high], array[low]

    QuickSortRecur(array, start, low - 1)
    QuickSortRecur(array, high + 1, end)

def quickSort(arr):  
    return [] if arr==[] else quickSort([y for y in arr[1:] if y<arr[0]]) + [arr[0]]+ quickSort([y for y in arr[1:] if y>=arr[0]])  

def partation(array, low, high):
    if low >= high:
        return
    pivotKey = array[low]
    while low < high:
        while array[high] >= pivotKey and low < high:
            high -= 1
        array[high], array[low] = array[low], array[high]
        while array[low] <= pivotKey and low < high:
            low += 1
        array[high], array[low] = array[low], array[high]
    return low

def QuickSortNonRecur(array):
    stack = []
    position = partation(array, 0, len(array) - 1)

    if position - 1 > 0:
        stack.append((0, position - 1))
    if position + 1 < len(array) - 1:
        stack.append((position + 1, len(array) - 1))
    while len(stack):
        low, high = stack[-1]
        stack.remove(stack[-1])
        mid = partation(array, low, high)
        if mid - 1 > low:
            stack.append((low, mid - 1))
        if mid + 1 < high:
            stack.append((mid + 1, high))
    return array

qsortlam = lambda arr: len(arrarr) > 1 and qsort(list(filter(lambda x: x <= arr[0], arr[1:]))) + arr[0:1] + qsort(list(filter(lambda x: x > arr[0], arr[1:]))) or arr


array = [8, 3, 1, 2, 5, 7, 6, 4, 7, 1, 89, 78, 21]
array = QuickSortNonRecur(array)
print(array)