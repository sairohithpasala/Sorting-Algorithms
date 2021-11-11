# Python program for INSERTION SORT
 

import timeit
#The main function to sort an array of given size using insertion sort
def insertionSort(arr):
 
    # scan/move through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # transfer elements of arr[0..i-1], that are > key, to one position ahead of their current place
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
 
 
# Main Code to pass input 
arr=[]        
n = int(input("Enter number of elements : "))
print ("Enter the array")
for i in range(0, n):
    ele = int(input())       #Input the data into the list
    arr.append(ele)
print ("Given array is", end="\n")
print(arr)
print('\n')
start = timeit.default_timer()
insertionSort(arr)              #passing the array to be sorted through function
print ("Sorted array by InsertionSort is:\t\t\t")
print(arr)
stop = timeit.default_timer()   
print("Execution Time is",stop - start,"seconds")
