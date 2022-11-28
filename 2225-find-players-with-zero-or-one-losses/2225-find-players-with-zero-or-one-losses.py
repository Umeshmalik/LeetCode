from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        lossers = defaultdict(int)
        for winner, losser in matches:
            winners.add(winner)
            lossers[losser] += 1
        always_winner = set()
        one_lost = set()
        for i in winners:
            if i not in lossers:
                always_winner.add(i)
            elif lossers[i] == 1:
                one_lost.add(i)
        for i in lossers:
            if lossers[i] == 1:
                one_lost.add(i)
        return [sorted(always_winner), sorted(one_lost)]