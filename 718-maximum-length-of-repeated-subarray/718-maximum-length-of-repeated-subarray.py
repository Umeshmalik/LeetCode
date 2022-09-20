class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        mx = 0
        for i in range(len(nums1)):
            curr = 0
            for j in range(len(nums2)):
                if i+j >= len(nums1): break
                if nums1[i+j] == nums2[j]:
                    curr += 1
                    mx = max(mx, curr)
                else: 
                    curr = 0
        for i in range(len(nums2)):
            curr = 0
            for j in range(len(nums1)):
                if i+j >= len(nums2): break
                if nums2[i+j] == nums1[j]:
                    curr += 1
                    mx = max(mx, curr)
                else: 
                    curr = 0
        return mx