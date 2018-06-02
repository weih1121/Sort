def InsertSort(array):
    j = 0
    length = len(array)
    for i in range(1, length):
        if array[i] < array[i - 1]:
            j = i
            while j > 0:
                if(array[j] < array[j - 1]):
                    array[j], array[j - 1] = array[j - 1], array[j]
                    j = j - 1
    return array



l = [49, 38, 65, 97, 76, 13, 27, 49]
l = InsertSort(l)
print(l)