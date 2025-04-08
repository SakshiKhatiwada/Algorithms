def Euclid(a, b):
    if b == 0:
        return a
    else:
        return Euclid(b, a % b)


print("The GCD is: ", Euclid(30, 21))
