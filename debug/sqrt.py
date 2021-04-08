def sqrt(i, eps):
    """Finds the square root of i with an error of at most eps"""
    r = i / 2
    while abs(i / r - r) > eps:
        r = (i / r + r) / 2
    return r

print(sqrt(9, 0.1), sqrt(16, 0.1), sqrt(20, 0.1))
