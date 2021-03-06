# Sort
排序算法

直接插入排序



直接插入排序是一种简单的排序算法，基本操作是将一个记录插入到一个有序结果集中，并且在插入数据过程中将前面大于或者小于(取决于升序或者降序)当前要插入的数据向后移动。

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

1. 时间复杂度O(n*n)
2. 额外空间复杂度O(1)
3. 稳定

---

希尔排序



1.插入排序在待排序列有序时可将插入排序的时间复杂度降至O(n)，基于此如果待排记录在进行插入排序之前基本有序则可以降低时间复杂度

2.此外直接插入排序算法比较简单，在n值很小时效率也比较高

基于上述2点改进插入排序->希尔排序。

希尔排序的增量dk取法：

1.Shell 增量序列的递推公式为： 

							ht=⌊N2⌋,hk=⌊hk+12⌋

2.Hibbard 增量序列的通项公式为： 

							hi=2i−1hi=2i−1

 Hibbard 增量序列的递推公式为： 

 							h1=1,hi=2∗hi−1+1h1=1,hi=2∗hi−1+1

Hibbard 增量序列的最坏时间复杂度为 Θ(N3/2)Θ(N3/2)；平均时间复杂度约为 O(N5/4)O(N5/4)。

3.Knuth 增量序列

Knuth 增量序列的通项公式为： 

							hi=12(3i−1)hi=12(3i−1)

 增量序列的递推公式为： 

							h1=1,hi=3∗hi−1+1

4.Gonnet 增量序列

Gonnet 增量序列的递推公式为： 

							ht=⌊N2.2⌋,hk=⌊hk+12.2⌋(若h2=2则h1=1)

5.Sedgewick 增量序列

Sedgewick 增量序列的通项公式为： hi=max(9∗4j−9∗2j+1,4k−3∗2k+1)hi=max(9∗4j−9∗2j+1,4k−3∗2k+1)

Sedgewick 增量序列的最坏时间复杂度为 O(N4/3)O(N4/3)；

平均时间复杂度约为 O(N7/6)O(N7/6)。

以Knuth 增量序列为基础的希尔排序算法如下：

    def ShellSort(array):
        dk, length, j = 0, len(array), 0
        while dk * 3 < length:
            dk = dk * 3 + 1
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
        return array

增量：dk 

待排序列长度:length 

j：用来处理当前数据对应减去dk的数据



1. 时间复杂度比较复杂在此不做讨论
2. 额外空间复杂度O(1)
3. 不稳定

---

冒泡排序



冒泡排序基本过程，比较相邻元素之间的大小关系，在一趟冒泡排序中可以从n个数据中选取最大或最小值(取决于升序还是降序),在循环过程中也就是从剩余的数据中依次选出其中最大或者最小值的过程。

冒泡排序非递归代码如下：

    def BubbleSort(array):
    
        length = len(array)
        for i in range(length - 1):
            for j in range(length - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array

length:数组长度

i:需要循环的次数

j:需要比较的次数

时间复杂度：O(n*n)

额外空间复杂度:O(1)

稳定的排序算法

冒泡排序递归代码如下：

    def BubbleSortRecur(array, end):
        
        if end == 0:
            return
        for i in range(end - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        BubbleSortRecur(array, end - 1)

end:表示循环需要比较到的最后一个位置



---

快速排序



快速排序是对冒泡排序的改进，通过一次排序将一个有序序列分成独立的两个部分，一部分比关键字小一部分比关键字大，再分别对其进行排序使得整个记录有序。

快排递归代码：

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

lambda版快排代码：

    qsortlam = lambda arr: len(arr) > 1 and qsort(list(filter(lambda x: x <= arr[0], arr[1:]))) + arr[0:1] + qsort(list(filter(lambda x: x > arr[0], arr[1:]))) or arr
    

短代码版：

    def quickSort(arr):  
        return [] if arr==[] else quickSort([y for y in arr[1:] if y<arr[0]]) + [arr[0]]+ quickSort([y for y in arr[1:] if y>=arr[0]])

非递归版本：

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

快排属于不稳定排序

平均时间复杂度为O(nlogn)

最差情况复杂度为O(n*n)

额外空间复杂度：O(n)

---

选择排序



选择排序就是在每次比较过程中拿一个值去和该值后边的所有值去比较，选择大的或者小的进行交换的过程。

选择排序代码：

    def SelectSort(array):
        if len(array) <= 1:
            return
    
        length = len(array)
        for i in range(length):
            for j in range(i + 1, length):
                if array[i] > array[j]:
                    array[i], array[j] = array[j], array[i]
        return array

选择排序属于不稳定排序算法

时间复杂度O(n*n)

额外空间复杂度为O(1)

---

堆排序



堆定义：简单讲堆是一个完全二叉树，满足根节点大于或小于左子树和右子树，根节点大的叫做大顶堆，反之叫做小顶堆。

堆排序是利用堆的性质，将堆顶作为要排序列的最后一个元素，因为堆顶是极大值。之后调整堆的结构，将后续的每个堆顶作为剩余序列的最后一个元素，直到整个序列只剩一个元素，排序结束。至于调整堆的具体过程在此并不过多描述，请参考算法导论堆排序相关问题。

根据上述想法堆排序可以编写递归版本的堆排序以及非递归版本的堆排序。

非递归版本的堆排序：

    def heapAdjast(array, start, leng):
        length, lchild = leng, 2 * start + 1                
        
        while lchild <= length - 1:
            if lchild + 1 > length - 1:
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
    
    def HeapSort(array):
        length = len(array)
    
        for i in range(length//2, 0, -1):
            heapAdjast(array, i - 1, len(array))
        for i in range(length - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            heapAdjast(array, 0, i)

注释：length需要调整的序列长度， length - 1需要调整的列表最后一个 ,lchild // 2指向根节点

递归版本堆排序：

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

递归版本相对比较容易理解

堆排序时间复杂度，O(nlogn)

空间复杂度:O(1)

不稳定排序

---

归并排序



归并排序是将一个序列拆分成一个一个元素，之后将两两相邻的元素放入一个新的列表中，依次类推最终将两个有序的列表归并成为一个新的列表，返回。

递归归并排序：

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

归并排序平均时间复杂度:O(nlogn)

额外空间复杂度：O(n)

稳定的排序算法

---

基数排序

基数排序是在桶排序的基础上，首先建立0-9的10个桶，之后分别对需要排序的序列的每个数，将该数的第i位取出，之后将整个数字放进对应的桶中，当每位数字都排列之后整个序列有序。排序方式可以从高位开始也可以从低位开始。

    import math
    
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

---

八大排序总结


