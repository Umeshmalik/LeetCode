class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        arr1 = [1] * N
        arr2 = [1] * N
        for i in range(1, N):
            arr1[i] = arr1[i-1] + 1 if ratings[i] > ratings[i-1] else 1
            arr2[N - i - 1] = arr2[N - i] + 1 if ratings[ N - i - 1] > ratings[N - i] else 1

        summ = 0
        for i in range(N):
            summ += max(arr1[i], arr2[i])
        return summ