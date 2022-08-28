class Solution:
    def trap(self, height: List[int]) -> int:
        arr1 = [0] * len(height)
        arr2 = [0] * len(height)
        mx = 0
        for i in range(0, len(height)):
            arr1[i] = max(height[i], mx)
            mx = arr1[i]
        mx = 0
        for i in range(len(height)-1, -1, -1):
            arr2[i] = max(height[i], mx)
            mx = arr2[i]
        sm = 0
        for i in range(len(height)):
            sm += min(arr1[i], arr2[i]) - height[i]
        return sm