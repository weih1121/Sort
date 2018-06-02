def mergeSort(array):
    length = len(array)
    if length < 2:
        return array

    mid = length // 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])

    result = []
    lPoint, rPoint = 0, 0
    while lPoint < len(left) and rPoint < len(right):
        if left[lPoint] < right[rPoint]:
            result.append(left[lPoint])
            lPoint += 1
        else:
            result.append(right[rPoint])
            rPoint += 1
    result += left[lPoint:] + right[rPoint:]
    return result

array = [8, 3, 1, 2, 5, 7, 6, 4, 7, 1, 89, 78, 21]
array = mergeSort(array)
print(array)