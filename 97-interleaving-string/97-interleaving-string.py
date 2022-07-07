class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def isInterleaving(X, Y, S):
            M, N = len(X), len(Y)
            if M + N != len(S):
                return False
            T = [[False for x in range(N + 1)] for y in range(M + 1)]
            for i in range(0, M + 1):
                for j in range(0, N + 1):
                    if i == 0 and j == 0:
                        T[i][j] = True
                    elif i and j and X[i - 1] == S[i + j - 1] and Y[j - 1] == S[i + j - 1]:
                        T[i][j] = T[i - 1][j] or T[i][j - 1]
                    elif i and X[i - 1] == S[i + j - 1]:
                        T[i][j] = T[i - 1][j]
                    elif j and Y[j - 1] == S[i + j - 1]:
                        T[i][j] = T[i][j - 1]
            return T[M][N]
        return isInterleaving(s1, s2, s3)