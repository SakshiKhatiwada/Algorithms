from timeit import default_timer as timer
import numpy as np


def MergeSort(A, first, last):
    if first == last:
        return
    mid = (first + last) // 2
    MergeSort(A, first, mid)
    MergeSort(A, mid + 1, last)
    simpleMerge(A, first, mid + 1, last)


def simpleMerge(A, first, second, last):
    i = first
    j = second
    temp = []

    while i < second and j <= last:
        # comparing with 2 arrays
        if A[i] < A[j]:
            temp.append(A[i])
            i = i + 1
        else:
            temp.append(A[j])
            j = j + 1

        # copying remaining elements, if one is finished before another
    while j <= last:
        temp.append(A[j])
        j = j + 1

    while i < second:
        temp.append(A[i])
        i = i + 1

        # copying to original array
    l = 0
    print('temp: ',temp)
    for index, value in enumerate(temp):
        A[first + index] = value


# driver's code

A = np.random.randint(0, 100000, 500)

# print(A, end=' ')
# print('len = ', len(A))
# print(A[500-1])

start = timer()
MergeSort(A, 0, len(A)-1)
stop = timer()

print("sorted: \n")
print(A, end=' ')
print("\n\ntime taken: ", stop - start)
