# Python program for BUBBLE SORT
import timeit  
def BSort(arr):
    n = len(arr)
  
    # Scan/move through all elements
    for i in range(n-1):
    # range(n) can also be taken, but it increases loop by +1, so we dont use it.
  
        
        for j in range(0, n-i-1):
  
            # Scan/ move through the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
  
# Main Code to pass input 
arr=[]        
n = int(input("Enter number of elements to be inserted in array : "))
print ("Enter the array")
for i in range(0, n):
    temp = int(input())    #Input the data into the list
    arr.append(temp)
print ("Given array is\n")
print(arr)
print('\n')
start = timeit.default_timer() 

BSort(arr)  #passing the array to be sorted through function
  
print ("Sorted array by BubbleSort is:\t\t\t")
print(arr)
stop = timeit.default_timer()   
print("Execution Time is",stop - start,"seconds")
