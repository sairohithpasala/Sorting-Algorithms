# Python program for QUICK SORT 3-MEDIAN
import timeit
def medianofthreepivots(arr, strt, endd):
    mid = (strt+endd-1)//2  #Considering all 3 pivots first , middle and last element as 3 median model
    l = arr[strt]
    m = arr[mid]
    o = arr[endd-1]                    #comparing the 3 pivot values with each other to find out the median of the 3 pivots
    if l <= m <= o:
        return m, mid
    if o <= m <= l:
        return m, mid
    if l <= o <= m:
        return o, endd-1
    if m <= o <= l:
        return o, endd-1
    return l, strt
#The main function to sort an array of given size using quick sort 3 median
def quicksortmed(arr, strt, endd, asc = True):
    result = 0
    if strt < endd:
        pivot_location, result = Partition(arr, strt, endd, asc)    #partitioning the array
        result += quicksortmed(arr, strt, pivot_location, asc)      #traverse from start index to pivot
        result += quicksortmed(arr, pivot_location + 1, endd, asc)   #traverse from pivot+1 to end index
    return result

#partition function for partitioning of the array
def Partition(arr, strt, endd, asc = True):
    result = 0
    pivotELE, pivotIDX = medianofthreepivots(arr, strt, endd)    # calling to get median of 3 pivot elements
    arr[strt], arr[pivotIDX] = arr[pivotIDX], arr[strt]
    i = strt + 1
    for j in range(strt+1, endd, 1):
        result += 1
        if (asc and arr[j] < pivotELE) or (not asc and arr[j] > pivotELE):    #checking for ascending or not and swapping the elements like usual quicksort
            arr[i], arr[j] = arr[j], arr[i]  
            i += 1
    arr[strt], arr[i-1] = arr[i-1], arr[strt]
    return i - 1, result

def quicksortmedian(arr, asc = True):
    quicksortmed(arr, 0, len(arr), asc)               #initially sending 0 as starting index and len(arr) which is ending index as pivots



# Main Code to pass input
arr=[]        
n = int(input("Enter number of elements : "))
print ("Enter the array")
for i in range(0, n):
    ele = int(input())            #Input the data into the list
    arr.append(ele)
print ("Given array is", end="\n")
print(arr)
print('\n')
start = timeit.default_timer()  
quicksortmedian(arr)                      #passing the array to be sorted through function
stop = timeit.default_timer()
print("Sorted array by quicksort 3-median is: \t\t\t")
print(arr)
print('\n')
print("Execution Time is",stop - start,"seconds")
