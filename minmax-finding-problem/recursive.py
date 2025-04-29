# Divide and Conquer
def MinMax(A, f_index, l_index, max, min):
    # base case, only 1 element
    if l_index == f_index:
        max = A[l_index]
        min = A[l_index]
        return (max, min)

    elif f_index == l_index - 1:  # only 2 elements
        if A[l_index] > A[f_index]:
            max = A[l_index]
            min = A[f_index]
        else:
            max = A[f_index]
            min = A[l_index]
        return (max, min)

    else:
        mid = (f_index + l_index) // 2
        max, min = MinMax(A, f_index, mid - 1, max, min)
        maxr, minr = MinMax(A, mid, l_index, max, min) # compares min, max for above's max min

        if max < maxr:
            max = maxr
        if min > minr:
            min = minr

        return (max, min)


# driver's code
A = [1, 2, 3, 9, 5, 3, 8, 5, 100, 2, -2, 45, 23, -3, 300, 400, 500]
max, min = MinMax(A, 0, len(A) - 1, None, None)
print("max: ", max, "min: ", min)
