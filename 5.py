def quicksort(arr,start,end):
    if start < end:
        pivot = partition(arr,start,end)
        quicksort(arr,start,pivot-1)
        quicksort(arr,pivot+1,end)
    return arr

def partition(arr,start,end):
    pivot = arr[end]
    i = start
    for j in range(start,end):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[end] = arr[end], arr[i]
    return i

arr = [77,43,6,8,3,2,6,8,32]
print(quicksort(arr,0,len(arr)-1))

######################################################

import random

def quicksortR(arr,start,end):
    if start < end:
        pivot = partition(arr,start,end)
        quicksort(arr,start,pivot-1)
        quicksort(arr,pivot+1,end)
    return arr

def partitionR(arr,start,end):
    rnd = random.randint(start,end)
    arr[rnd], arr[end] = arr[end], arr[rnd]
    pivot = arr[end]
    i = start
    for j in range(start,end):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[end] = arr[end], arr[i]
    return i

arr = [77,43,6,8,3,2,6,8,32]
print(quicksortR(arr,0,len(arr)-1))