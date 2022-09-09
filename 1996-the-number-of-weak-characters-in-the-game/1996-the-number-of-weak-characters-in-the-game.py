class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x:(-x[0],x[1]))
        count = mx = 0
        for a,d in properties:
            if d <mx:
                count+=1
            mx = max(d,mx)
        return count