# Python program for HEAP SORT
import timeit
# To heapify subtree rooted at index m. n = size of heap
def heapify(arr, n, m):
    largest = m  # Initialize largest as the root
    lft = 2 * m + 1     # left = 2*m + 1
    rght = 2 * m + 2     # right = 2*m + 2
  
    # Check if left child of root exists and is > root
    if lft < n and arr[m] < arr[lft]:
        largest = lft
  
    # Check if right child of root exists and is > root
    if rght < n and arr[largest] < arr[rght]:
        largest = rght
  
    # Change root, if required
    if largest != m:
        arr[m],arr[largest] = arr[largest],arr[m]  # Swapping
  
        # Heapify the root(recursive).
        heapify(arr, n, largest)
  
# The main function to sort an array of given size using heapsort
def heapSort(arr):
    n = len(arr)
  
    # Build a maxheap.
    # As last parent will be at ((n//2)-1) location, we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
  
    # Extraction of elements one by one
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # Swapping
        heapify(arr, i, 0)
  
# Main Code to pass input 
arr=[]        
n = int(input("Enter number of elements : "))
print ("Enter the array")
for i in range(0, n):
    ele = int(input())     #Input the data into the list
    arr.append(ele)
print ("Given array is", end="\n")
print(arr)
print('\n')
start = timeit.default_timer()
heapSort(arr)   #passing the array to be sorted through function
print ("Sorted array by HeapSort is:\t\t\t")
print(arr)
stop = timeit.default_timer()   
print("Execution Time is",stop - start,"seconds")