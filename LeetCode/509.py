"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
"""


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

# or


def fibonacci2(n):
    if n == 0:
        return 0
    n1 = 1
    n2 = 1
    # (1, n - 2) because start by 1, 2, 3... not 0, 1, 1, 2, 3....
    for i in range(1, n - 2):
        n1 += n2
        n2 = n1 - n2
    return n1
