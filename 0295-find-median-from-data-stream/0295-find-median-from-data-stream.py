import heapq

class MedianFinder:

    def __init__(self):
        self.arr = []
        
    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        size = len(self.arr)
        self.arr.sort()
        return self.arr[math.ceil(size/2)-1] if size&1 else (self.arr[size//2] + self.arr[(size//2)-1]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()