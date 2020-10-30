import random
def quickSort(arr, start, end):
    '''Quick Sort Algorithm'''
    '''Worst Case: O(n^2). Occurs when pivot is greatest or smallest item.'''
    '''Best Case: Ω(n*log(n))'''
    '''Average: O(n*log(n))'''
    if len(arr) <= 1:
        return arr
    
    if start < end:
        i = partition(arr, start, end)
        quickSort(arr, start, i-1) #sort partition to the left of i, and to the right
        quickSort(arr, i+1, end)    
    return arr
    
def partition(arr, start, end):
    i = start-1 #index of smaller element
    pivot = arr[end] 
    for j in range(start, end):
        if arr[j] <= pivot:
            i+= 1
            arr[i], arr[j] = arr[j], arr[i] #swap j and i values
    #value is greater than the pivot
    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i+1

A = [random.randint(1,100) for i in range(10)]
print(A)
print(quickSort(A, 0, len(A)-1))


#alternative solution, not in place
def quicksort(arr):
    if not arr:
        return []
    pivot = arr[0]
    smaller_items = quicksort([a for a in arr[1:] if a <= pivot])
    larger_items = quicksort([a for a in arr[1:] if a > pivot])
    return smaller_items + [pivot] + larger_items

print("\nNot in place:")
print(quicksort(A))