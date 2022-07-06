class Solution:
    def fib(self, n: int) -> int:
        first = second = 1
        if n == 0 : return 0
        for i in range(2, n):
            second , first = first + second , second
        return second