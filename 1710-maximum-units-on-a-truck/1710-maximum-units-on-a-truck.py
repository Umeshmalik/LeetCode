class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda row: (row[1]), reverse = True )
        sum = 0
        i = 0
        while i < len(boxTypes) and truckSize > 0:
            if truckSize >= boxTypes[i][0]:
                sum += boxTypes[i][0] * boxTypes[i][1]
                truckSize -= boxTypes[i][0]
                i+=1
            else:
                sum += boxTypes[i][1] * truckSize
                truckSize = 0
                i += 1
        return sum