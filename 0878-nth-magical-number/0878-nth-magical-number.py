class Solution:
    def nthMagicalNumber(self, A: int, B: int, C: int) -> int:
        LCM = (B * C) // math.gcd(B, C)
        left = 1
        right = sys.maxsize

        def check(mid):
            return (mid // B + mid // C - mid // LCM) >= A;

        while left < right :
            mid = left + (right - left)//2;
            if check(mid): right = mid
            else: left = mid + 1

        return left % 1000000007