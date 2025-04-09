# This theory was first introduced by Sun-Tsu


def Chinese_Remainder_Theorem(a, m):  # a and m are arrays
    M = 1  # to find multiplication
    z = []
    # z_inv = []  # for z inverse modulo m_i
    w = []
    y = []
    x = 0

    for i in range(0, len(m)):
        M *= m[i]

    # calculating z[]
    for i in range(0, len(m)):
        z.append(M // m[i])

    # calculating y[] and w []
    for i in range(0, len(m)):
        j = 1
        while True:
            if z[i] * j % m[i] == 1:  # finding the inverse of z_i
                y.append(j % m[i])
                w.append(y[i] * z[i] % M)
                break
            j += 1
        x += a[i] * w[i]

    print("a: ", a, "\nm: ", m, "\nz: ", z, "\ny: ", y, "\nw: ", w)
    return x % M, M


# driver's code
# a = [2, 3]
# m = [5, 13]

a = [1, 3, 6]
m = [2, 5, 7]
x, M = Chinese_Remainder_Theorem(a, m)
print(f"The x we are finding for is: {x}")
print(f"All solutions: {x}+{M}k")
