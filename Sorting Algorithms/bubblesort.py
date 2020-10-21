def bubbleSort(arr):
    '''Bubble Sort Algorithm'''
    '''Time Complexity: O(n^2)'''
    '''O(n) if data is nearly sorted'''
    i = 0
    while i < len(arr)-1: #elements in bubble sort are sorted and moved to the top
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            i = 0
            continue
        i+=1
    return arr

A = [64, 25, 12, 22, 11] 
print(bubbleSort(A))