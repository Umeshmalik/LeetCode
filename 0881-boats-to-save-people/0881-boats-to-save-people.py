class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0
        i = 0
        j = len(people) - 1
        while i <= j:
            if people[j] + people[i] <= limit:
                ans += 1
                i += 1
                j -= 1
            else:
                ans += 1
                j -= 1
        return ans
            