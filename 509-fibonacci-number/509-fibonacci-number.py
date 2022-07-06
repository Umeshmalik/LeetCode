class Solution:
    def fib(self, n: int) -> int:
        first = second = 1
        if n == 0 : return 0
        if n == 1 or n == 2: return 1
        for i in range(2, n):
            temp = second
            second += first
            first = temp
        return second