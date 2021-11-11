
ip = int(input("Enter you choice- \n1. Mergesort \n2. Heapsort \n3. Regular quick sort \n4. quick sort using 3 medians \n5. Insertion Sort \n6. Selection Sort \n7. Bubble Sort \n8. Exit Main Menu\n"))
if ip == 1:
    exec(open('Mergesort.py').read())
    exec(open('MainMenu.py').read())
elif ip == 2:
    exec(open('HeapSort.py').read())
    exec(open('MainMenu.py').read())
elif ip == 3:
    exec(open('quicksortrecursive.py').read())
    exec(open('MainMenu.py').read())
elif ip == 4:
    exec(open('quicksort3median.py').read())
    exec(open('MainMenu.py').read())
elif ip == 5:
    exec(open('InsertionSort.py').read())
    exec(open('MainMenu.py').read())
elif ip == 6:
    exec(open('SelectionSort.py').read())
    exec(open('MainMenu.py').read())
elif ip == 7:
    exec(open('BubbleSort.py').read())
    exec(open('MainMenu.py').read())
elif ip == 8:
    exit()
else:
    print("Invalid Option,Please Select correct option and Try again")
    exec(open('MainMenu.py').read())
