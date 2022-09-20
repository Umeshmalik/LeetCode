class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums2_str = ''.join([chr(x) for x in nums2])       
        max_str = ''
        res = 0
        
        for i in nums1:
            max_str += chr(i)
            
            if max_str in nums2_str:
                res = max(res, len(max_str))  
            else: 
                max_str = max_str[1:]
            
        return res