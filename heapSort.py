def heapAdjast(array, start, leng):
    length, lchild = leng, 2 * start + 1                        #leng需要调整的序列长度， length - 1需要调整的列表最后一个
    
    while lchild <= length - 1:
        if lchild + 1 > length - 1:                                 #右子树不存在
            if array[lchild // 2] < array[lchild]:
                array[lchild], array[lchild // 2] = array[lchild // 2], array[lchild]
            return
        else:
            tmp = max(array[lchild], array[lchild + 1])
            if tmp <= array[lchild // 2]:
                return
            if tmp == array[lchild]:
                array[lchild // 2], array[lchild] = array[lchild], array[lchild // 2]
                lchild = lchild * 2 + 1                   
            elif tmp == array[lchild + 1]:
                array[lchild // 2], array[lchild + 1] = array[lchild + 1], array[lchild // 2]
                lchild = (lchild + 1) * 2 + 1

 def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)
 
def heap_sort(lists):
    size = len(lists)
    for i in range(0, (size/2))[::-1]:
        adjust_heap(lists, i, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
        
def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)

def HeapSort(array):
    length = len(array)

    for i in range(length//2, 0, -1):
        heapAdjast(array, i - 1, len(array))
    for i in range(length - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapAdjast(array, 0, i)

array = [8, 3, 1, 2, 5, 7, 6, 4, 7, 1, 89, 78, 21]
HeapSort(array)
print(array)