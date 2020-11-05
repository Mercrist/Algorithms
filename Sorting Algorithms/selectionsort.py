def selSort(arr):
    '''Selection Sort Algorithm'''
    '''Average Case: O(n^2)'''
    '''Best Case: Ω(n^2)'''
    '''Worst Case: Θ(n^2)'''
    for i in range(len(arr)): #i loop will go forward and check to swap with the next smallest value at the start of the arr 
        potentialSmallest = i
        for j in range(i+1, len(arr)): #goes through array, finds smallest value, swaps, proceeds with above
            if arr[j] < arr[potentialSmallest]:
                potentialSmallest = j
        arr[i], arr[potentialSmallest] = arr[potentialSmallest], arr[i] #swap values
    return arr
    
A = [64, 25, 12, 22, 11] 
print(selSort(A))

