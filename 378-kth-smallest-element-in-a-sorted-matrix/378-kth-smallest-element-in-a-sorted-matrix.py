#this will take n^2 time to compute, which is not recommended

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted([i for j in matrix for i in j])[k-1]