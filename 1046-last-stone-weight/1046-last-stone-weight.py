class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        from sortedcontainers import SortedList
        li = SortedList(stones)
        while len(li) > 1:
            a = li.pop()
            b = li.pop()
            li.add(a-b)
        return li.pop()
            