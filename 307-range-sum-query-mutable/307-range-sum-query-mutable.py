class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.s = sum(nums)

    def update(self, index: int, val: int) -> None:
        diff = val - self.arr[index]
        self.s += diff
        self.arr[index] = val

    def sumRange(self, left: int, right: int) -> int:
        l = sum([self.arr[i] for i in range(0, left)])
        r = sum([self.arr[i] for i in range(right+1, len(self.arr))])
        return self.s - l - r

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)