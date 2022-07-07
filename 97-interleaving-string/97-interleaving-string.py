class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        d = {}
        def isInterleaving(X, Y, S, T):
            if not X and not Y and not S:
                return True
            if not S:
                return False
            key = (X, Y, S)
            if key not in T:
                x = (len(X) and S[0] == X[0]) and isInterleaving(X[1:], Y, S[1:], T)
                y = (len(Y) and S[0] == Y[0]) and isInterleaving(X, Y[1:], S[1:], T)
                T[key] = x or y
            return T[key]
        return isInterleaving(s1, s2, s3, d)