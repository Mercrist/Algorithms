def mergeSort(arr):
    '''Insertion Sort Algorithm'''
    '''Time Complexity: O(n*log(n))'''
    if len(arr) <= 1: #base case
        return arr
    
A = [64, 25, 12, 22, 11] 
print(mergeSort(A))