class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isOk(cap):
            curr = 0
            day = 1
            for weight in weights:
                if curr + weight > cap:
                    curr = weight
                    day += 1
                else:
                    curr += weight
            return day <= days
            
        mn, mx = max(weights), sum(weights)
        while mn < mx:
            mid = mn + (mx - mn) // 2
            if isOk(mid):
                mx = mid
            else:
                mn = mid + 1
        return mn