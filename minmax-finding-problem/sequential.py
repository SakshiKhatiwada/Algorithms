import sys

def MinMax(A):
    size = len(A)
    max = -sys.maxsize-1
    min = sys.maxsize
    print(min,max)
    i = 0
    while i < size:
        if A[i] < min:
            min = A[i]
        if A[i] > max:
            max = A[i]
        i = i + 1
        
    return (max,min)

print(MinMax([2,3,5,9,1,100]))