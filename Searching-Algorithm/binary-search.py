def Binary_Search(A, first_index, last_index, key):
    """
    It takes an already sorted array and search for the given key. Time Complexity: O(logn)
    """
    # base case
    if first_index == last_index:
        if key == A[first_index]:
            return first_index
        else:
            print("key not found")
            return "error"

    # recursive case
    mid = (first_index + last_index) // 2  # floor value
    if key == A[mid]:
        return mid
    else:
        if key < A[mid]:
            return Binary_Search(A, first_index, mid - 1, key)
        else:
            return Binary_Search(A, mid + 1, last_index, key)


# driver's code
A = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]
result = Binary_Search(A, 0, len(A) - 1, key=6)
print("resulting index: ", result)
