import time
import math
def test():
    start_time = time.time()
    for a in range(0,1001):
        for b in range(0,1001):
            for c in range(0,1001):
                if a**2+b**2 == c**2 and a+b+c == 1000:
                    print('a,b,c:%d,%d,%d' % (a,b,c,))
    
    end_time = time.time()
    print('elapsed:%f' % (end_time - start_time))
    print('complete')

#冒泡排序
def bubble_sort(l):
    for j in range(len(l)-1,0,-1):
        for i in range(j):
            if l[i] > l[i+1]:
                l[i],l[i+1] = l[i+1],l[i]
    print(l)


#选择排序
def selectionSort(array):
    for i in range(len(array) - 1):
        minIndex = i
        for j in range(i + 1,len(array)):
            if array[i] < array[minIndex]:
                minIndex = j
            if i != minIndex:
                array[i],array[minIndex] = array[minIndex],array[i]
    print(array)



#插入排序
def insertSort(array):
    for i in range(1,len(array)):
        preIndex = i - 1
        current = array[i]
        while array[preIndex] > current:
            array[preIndex+i] = array[preIndex]
            preIndex-= 1
        array[preIndex+1] = current
    print(array)

#希尔排序
def shellSort(array):
    gap = 1
    while gap < len(array)/3:
        gap = gap * 3 +1
    while gap >0:
        for i in range(gap, len(array)):
            temp = array[i]
            j = i - gap
            while j >=0 and array[i] > temp:
                array[j + gap] = array[i]
                j-= gap
            array[j + gap]
        gap = math.floor(gap/3)
    print(array)


#归并排序
def mergeSort(array):
    if len(array) < 2:
        return array
    middle = math.floor(len(array)/2)
    left,right = array[0:middle],array[middle:]
    return merge(mergeSort(left),mergeSort(right))

def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

#快速排序
def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(arr)-1 if not isinstance(right,(int,float)) else right
    if left < right:
        partitionIndex = partition(arr,left,right)
        quickSort(arr,left,partitionIndex-1)
        quickSort(arr,partitionIndex+1,right)
    return arr
def partition(arr,left,right):
    pivot = left
    index = pivot+1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr,i,index)
            index+=1
        i+=1
    swap(arr,pivot,index-1)
    return index-1

def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]


if __name__ == '__main__':
        # test()
    l = [54,26,93,17,77,31,44,55,20]
    bubble_sort(l)
    selectionSort(l)
    insertSort(l)
    shellSort(l)