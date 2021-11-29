def find_factorial_recursive(number):  # O(n)......
    if number == 2:
        return 2
    return number * find_factorial_recursive(number-1)


def find_factorial_iterative(number):  # O(n)
    answer = 1
    for num in range(1, number+1):
        answer = answer * num
    return answer


print(find_factorial_recursive(5))
# print(find_factorial_iterative(5))
