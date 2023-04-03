class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0
        i = 0
        j = len(people) - 1
        while i <= j:
            i += 1 if people[j] + people[i] <= limit else 0
            j -= 1
            ans += 1
        return ans
            