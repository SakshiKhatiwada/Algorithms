SIZE = 4  # defining constant N
tup = [0] * SIZE  # initializing empty list

# SECTION function


def nQueen(tup, row):
    """
    The Famous n-Queen problem where it is needed to put n Queens on a nxn board such that no queen is attacking another.

    Representation:
    indices of list 'tup': rows
    values of 'tup': cols
    diagonal values: /difference in rows/ = /difference in cols/

    Attributes:
    tup: the list containing the position of the Queens on the board
    row: the current row we are checking
    """
    for col in range(0, SIZE):  # represents the values in the tuple
        tup[row] = col

        if row == SIZE - 1 and not isAttacked(tup, row):
            print("tuple:", tup)

        if not isAttacked(tup, row):
            nQueen(tup, row + 1)


def isAttacked(tup, row):
    """
    This checks whether the position at which the queen is is getting attacked or attacking or not.
    """

    for i in range(0, row):
        if tup[i] == tup[row] or abs(tup[i] - tup[row]) == abs(i - row):
            # checking the col values, checking the diagonal values
            return True
        else:
            return False


# SECTION Driver's code
# nQueen(tup, 0)
print(tup[4])
