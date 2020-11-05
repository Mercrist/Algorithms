from random import randint
def heapSort(arr, end):
    '''Heap Sort Algorithm'''
    '''Average Case: O(n*log(n))'''
    '''Best Case: Ω(n*log(n))'''
    '''Worst Case: Θ(n*log(n))'''
    if end <= 0 or len(arr) <= 1: #algorithm ends when there's one element or less
        return arr
    buildHeap(arr, end)
    arr[0], arr[end] = arr[end], arr[0]
    end -= 1
    return heapSort(arr,end)    
    


def buildHeap(arr, end):
    '''Builds the Max Heap'''
    if end <=0: #recursively max heap half of arr to the start
        return arr

    i = (end-1)//2 #parent
    while i >= 0: #index backwards, swapping the parent with the bigger of each child 
        leftChild = 2*i+1
        rightChild = 2*i+2

        #https://stackoverflow.com/questions/64687514/heapsort-code-works-on-smaller-arrays-but-not-bigger-ones
        if arr[leftChild] > arr[i] and (rightChild > end or arr[leftChild] > arr[rightChild]):  #access left child first, so it doesnt check right child
            arr[i], arr[leftChild] = arr[leftChild], arr[i] 
            #swaps left child when it's bigger than its parent, there is no rightChild, OR leftChild is greater than rightChild value

        elif rightChild <= end and arr[rightChild] > arr[i]: #doesn't have to compare leftChild again
            arr[i], arr[rightChild] = arr[rightChild], arr[i] #else, if rightChild is less than or equals to max index and greater than parent, swap
        i-=1
    return buildHeap(arr, i) #instead of build heaping through each node, only build heap up to the next parent 

A = [randint(1,100) for i in range(20)]
print(heapSort(A, len(A)-1)) 