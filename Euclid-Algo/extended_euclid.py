def ext_euclid(a, b):
    if b == 0:
        return [a, 1, 0]
    else:
        [d1, x1, y1] = ext_euclid(b, a % b)
        [d, x, y] = [d1, y1, x1 - (a // b) * y1]
        return [d, x, y]


a = 99
b = 78
[d, x, y] = ext_euclid(a, b)
print(f"From ax+by, x, y and gcd of {a} and {b}  are: ", x, y, d)
