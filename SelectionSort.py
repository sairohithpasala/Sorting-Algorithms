# Python program for SELECTION SORT

import timeit

def SelectSort(Arr):
    
# Traverse through all array elements
    for i in range(len(Arr)):
      
    # gather the minimal element in remaining unsorted array 
        min_index = i
        for j in range(i+1, len(Arr)):
            if Arr[min_index] > Arr[j]:
                min_index = j
              
    # Swap the found min element with the first       
        Arr[i], Arr[min_index] = Arr[min_index], Arr[i]
  
# Main Code to pass input

Arr=[]        
n = int(input("Enter number of elements : "))
print ("Enter the array")
for i in range(0, n):
    ele = int(input())                 #Input the data into the list
    Arr.append(ele)
print ("Given array is", end="\n")
print(Arr)
print('\n')
start = timeit.default_timer()
SelectSort(Arr)                                        #passing the array to be sorted through function
print ("Sorted array with Selection Sort is: \t\t\t")
print(Arr)
stop = timeit.default_timer()   
print("Execution Time is",stop - start,"seconds")
