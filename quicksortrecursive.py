# Python program for QUICK SORT
import timeit

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # Check if the current value we're looking at is > pivot then it is in the right place (right side of pivot) and we can move left,to the next element.
        # Also, we need to make sure that we haven't crossed the low pointer, since that would mean we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # viceversa process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # If we either got a value for both high and low that is out of order (or) low is > than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
    
        else:
          
            break        #exit loop

    array[start], array[high] = array[high], array[start]

    return high
 #The main function to sort an array of given size using quick sort   
def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
# Main Code to pass input 
array=[]        
n = int(input("Enter number of elements : "))
print ("Enter the array")
for i in range(0, n):
    ele = int(input())       #Input the data into the list
    array.append(ele)
print ("Given array is", end="\n")
print(array)
print('\n')
start = timeit.default_timer()
quick_sort(array, 0, len(array) - 1)                        #passing the array to be sorted through function
print("Sorted array by QuickSort is: \t\t\t")
print(array)
stop = timeit.default_timer()   
print("Execution Time is",stop - start,"seconds")
