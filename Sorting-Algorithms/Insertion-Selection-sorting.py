# SECTION Insertion Sort
def Insertion_Sort(array):
    n = len(array)
    i = 1  # initially

    while i <= n - 1:
        key = array[i]

        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key
        i = i + 1

    # printing
    print("Sorting with Insertion Sort")
    for item in array:
        print(item, end=" ")
    print('\n')


# SECTION Selection Sort
def Selection_Sort(array):
    n = len(array)
    i = 0
    while i < n - 1:
        min_index = i
        j = i + 1
        while j < n:
            if array[min_index] > array[j]:
                min_index = j
            j = j + 1

        # swapping
        array[min_index], array[i] = array[i], array[min_index]
        i = i + 1
        
    # printing
    print("Sorting with Selection Sort")
    for item in array:
        print(item,end=' ')
    print('\n')


# driver's code
Insertion_Sort([4, 1, 9, 2, 7])
Selection_Sort([4, 1, 9, 2, 7])
