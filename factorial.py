# C помощью функции factorial модуля math
import math

print(math.factorial(5))


# Итеративный подход
def factorial_i(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


print(factorial_i(5))


#  Рекурсивный подход
def factorial_r(n):
    if n < 2:
        return 1
    else:
        return n * factorial_r(n - 1)


print(factorial_r(5))
