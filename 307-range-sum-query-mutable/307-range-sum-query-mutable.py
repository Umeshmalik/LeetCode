class NumArray:

    def __init__(self, nums: List[int]):
        '''
            initialy store initial array and sum of whole array
        '''
        self.arr = nums
        self.s = sum(nums)

    def update(self, index: int, val: int) -> None:
        '''
             for every update operation calculate new sum by taking difference between new value 
             and number previously on that index, and add/minus that differ from sum 
             and set new value to that index in array
        '''
        diff = val - self.arr[index]
        self.s += diff
        self.arr[index] = val

    def sumRange(self, left: int, right: int) -> int:
        '''
            calculate sum of numbers before left index and 
            numbers after number after right index and minus them from sum 
            and return remaining answer
        '''
        to_minus = sum([self.arr[i] for i in range(0, left)] + [self.arr[i] for i in range(right+1, len(self.arr))])
        return self.s - to_minus

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)