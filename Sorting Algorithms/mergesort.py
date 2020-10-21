def mergeSort(arr):
    '''Merge Sort Algorithm'''
    '''Time Complexity: Consistently O(n*log(n))'''
    if len(arr) <= 1: #base case
        return arr

    left = mergeSort(arr[0:len(arr)//2]) #split list into 2 parts, recursively, until they are split into a single list
    right = mergeSort(arr[len(arr)//2:])
    return merge(left, right) #sorts and merges the 2 split but sorted lists
    
def merge(half1, half2):
    '''Merges the split arrays'''
    i = 0
    j = 0
    sortList = []
    while i < len(half1) and j < len(half2):
        if half1[i] <= half2[j]: #compares one element from one list to the other
            sortList.append(half1[i])
            i += 1
        else: #appends the right order to the sorted list, continues comparing
            sortList.append(half2[j])
            j += 1
            
    sortList.extend(half1[i:]) #merges the sorted sublists into one list
    sortList.extend(half2[j:])
    return sortList

A = [64, 25, 12, 22, 11]
print(mergeSort(A)) 