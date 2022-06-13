class Solution:
    def minimumTotal(self, arr: List[List[int]]) -> int:
        if len(arr) == 1:
            return arr[0][0]
        cache = [arr[0]]
        cache.append([])
        cache[1].append(arr[1][0] + cache[0][0])
        cache[1].append(arr[1][1] + cache[0][0])
        for i in range(2, len(arr)):
            cache.append([])
            for j in range(len(arr[i])):
                if j == 0:
                    cache[i].append(arr[i][j] + cache[i-1][j])
                elif j == len(arr[i]) - 1:
                    cache[i].append(arr[i][j] + cache[i-1][j-1])
                else:
                    cache[i].append(arr[i][j] + min(cache[i-1][j-1], cache[i-1][j]))
        return min(cache[-1])