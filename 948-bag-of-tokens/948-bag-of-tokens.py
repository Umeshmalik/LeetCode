class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i = 0
        j = len(tokens) - 1
        score = 0
        while i <= j:
            if score < 0: return 0
            if power >= tokens[i]:
                score += 1
                power -= tokens[i]
                i += 1
            else:
                if i != j:
                    score -= 1
                power += tokens[j]
                j -= 1
        return score