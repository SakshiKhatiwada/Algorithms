# Building Heap, calling heapify for each parent
def Build_Heap(A):
    heapsize = len(A)

    # for i = heapsize//2 to 1st element
    i = heapsize // 2
    while i >= 0:
        Heapify(A, i, heapsize)
        i = i - 1


# Heapify, to make sure it's a heap
def Heapify(A, i, heapsize):
    l = 2 * i + 1  # left child
    r = 2 * i + 2  # right child

    if l < heapsize and A[l] > A[i]:
        max = l
    else:
        max = i

    if r < heapsize and A[r] > A[max]:
        max = r

    if max != i:
        A[i], A[max] = A[max], A[i]  # swap
        Heapify(A, max, heapsize)


# Heap Sort, finally sorting element
def Heap_Sort(A):
    Build_Heap(A)  # Building Heap, calling heapify for each parent

    i = len(A) - 1  # upto n-1 position only
    while i > 0:
        A[0], A[i] = A[i], A[0]  # swap the ith element from last with the first node
        i = i - 1
        # remove last node from the count (we could have taken 2 var to make it less confusing)
        Heapify(
            A, 0, heapsize=i
        )  # we are logically removing the last element, so inform Heapify() about that

    # printing
    for item in A:
        print(item, end=" ")


# driver's code:
Heap_Sort([1, 2, 45, 89, 32, 83, 21, 8, 23])
