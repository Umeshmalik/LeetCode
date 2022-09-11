class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        perf = sorted(zip(speed, efficiency), key=lambda x: -x[1])
        total_speed = 0
        hp = []
        best = 0
        
        for s, e in perf:
            total_speed += s
            heapq.heappush(hp, s)
            if len(hp) > k:
                total_speed -= heapq.heappop(hp)
            best = max(best, total_speed * e)
            
        return best % mod