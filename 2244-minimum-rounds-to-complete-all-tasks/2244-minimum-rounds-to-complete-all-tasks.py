from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        values = Counter(tasks).values()
        if 1 in values: return -1
        count = 0
        for value in values:
            if value%3 == 0: count += value//3
            elif value%3 == 1: count += (1 if value == 2 else 2) + (value-4)//3
            else: count += 1 + (value-2)//3
        return count