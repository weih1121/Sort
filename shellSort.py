def ShellSort(array):
    dk, length, j = 0, len(array), 0
    while dk * 3 < length:
        dk = dk * 3 + 1
    print(dk, length)
    while dk > 0:
        for i in range(dk, length):
            if (array[i] < array[i - dk]):
                tmp = array[i]
                j = i - dk
                while j >= 0 and array[j] > tmp:
                    array[j + dk] = array[j]
                    j -= dk
                array[j + dk] = tmp
        dk //= 3
        print(array)
    return array

array = [8, 3, 1, 2, 5, 7, 6, 4, 7, 1, 89, 78, 21]
array = ShellSort(array)
print(array)