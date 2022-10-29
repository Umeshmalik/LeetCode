import heapq

class MedianFinder:

    def __init__(self):
        self.arr = []
        
    def addNum(self, num: int) -> None:
        self.arr.insert(self.getPos(num), num)

    def findMedian(self) -> float:
        size = len(self.arr)
        return self.arr[math.ceil(size/2)-1] if size&1 else (self.arr[size//2] + self.arr[(size//2)-1]) / 2
    
    def getPos(self, val):
        arr = self.arr
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = start + (end-start) // 2
            if arr[mid] == val:
                return mid
            elif arr[mid] < val:
                start = mid + 1
            else:
                end = mid - 1
        return start

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()