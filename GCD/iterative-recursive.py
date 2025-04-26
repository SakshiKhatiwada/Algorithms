# Iterative Approach
def GCD_iterative(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


# Recursive Approach
def GCD_recursive(a, b):
    if b == 0:
        return a
    else:
        return GCD_recursive(b, a % b)


# driver's code
a = 5
b = 6
print("GCD of two number ", a, "and", b, "=", GCD_iterative(a, b))
print("GCD of two number ", a, "and", b, "=", GCD_recursive(a, b))
