def fibonacci_iterative(n):  # O(n)
    a = 0
    b = 1
    total = 0
    for i in range(n-1):
        total = a + b
        a = b
        b = total
    return total


def fibonacci_recursive(n):  # O(2^n)
    if n < 2:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


print(fibonacci_iterative(21))
print(fibonacci_recursive(21))
