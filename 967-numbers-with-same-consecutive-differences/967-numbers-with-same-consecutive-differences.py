class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.arr = set()
        def get(st, nxt):
            if nxt > 9 or nxt < 0 or len(st) > n: return None
            st = st + str(nxt)
            if len(st) == n: self.arr.add(st)
            get(st, nxt-k)
            get(st, nxt+k)
            return None
        for i in range(1, 10):
            for j in range(n):
                get("", i)
        return self.arr