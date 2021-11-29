def reverse_string_iteration(string):
    return string[::-1]


def reverse_string_recursion(string):
    size = len(string)
    if size == 0:
        return ""
    last_char = string[size - 1]
    print(last_char, end='')
    return reverse_string_recursion(string[0:size - 1])


# print(reverse_string_iteration("salut"))
print(reverse_string_recursion("salut"))
