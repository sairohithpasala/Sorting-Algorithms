# Python program for MERGE SORT
import timeit
#The main function to sort an array of given size using merge sort
def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the middleindex of the array
        middleindex = len(arr)//2
 
        # Dividing the array elements into 2 halves
        Lft = arr[:middleindex]
        Rght = arr[middleindex:]
 
        # Sorting the first half
        mergeSort(Lft)
 
        # Sorting the second half
        mergeSort(Rght)
 
        i = j = k = 0
 
        # Transfer data to temporary arrays Lft[] and Rght[]
        while i < len(Lft) and j < len(Rght):
            if Lft[i] < Rght[j]:
                arr[k] = Lft[i]
                i += 1
            else:
                arr[k] = Rght[j]
                j += 1
            k += 1
 
        # Seeing if any element was left
        while i < len(Lft):
            arr[k] = Lft[i]
            i += 1
            k += 1
 
        while j < len(Rght):
            arr[k] = Rght[j]
            j += 1
            k += 1
 
# Main Code to pass input 
arr=[]        
n = int(input("Enter number of elements : "))
print ("Enter the array")
for i in range(0, n):
    ele = int(input())              #Input the data into the list
    arr.append(ele)
print ("Given array is", end="\n")
print(arr)
print('\n')
start = timeit.default_timer()
mergeSort(arr)              #passing the array to be sorted through function
print ("Sorted array by MergeSort is:\t\t\t")
print(arr)
stop = timeit.default_timer()   
print("Execution Time is",stop - start,"seconds")
