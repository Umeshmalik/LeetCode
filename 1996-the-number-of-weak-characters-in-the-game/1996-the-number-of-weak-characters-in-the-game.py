class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0],x[1])) #attach desc, def increase
        res=0
        max_defense=0
        for i in range(len(properties)):
            d=properties[i][1]
            if d>=max_defense :
                max_defense=max(d, max_defense)
            else:
                res+=1
        return res
            