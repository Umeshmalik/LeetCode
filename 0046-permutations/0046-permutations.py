class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def fact(k):
            ans = 1
            for i in range(k, 0, -1): ans *= i
            return ans
        arr = []
        per = fact(len(nums))
        for i in range(1, per+1):
            t1 = i
            n = len(nums) - 1
            block_size = fact(n)
            temp = [*nums]
            ans = []
            while len(temp) > 1:
                pos = (t1-1) // block_size
                ans.append(temp[pos])
                temp = temp[:pos] + temp[pos+1:]
                t1 = t1 - pos * block_size
                block_size //= n
                n -= 1
            ans += temp
            arr.append(ans)
        return arr