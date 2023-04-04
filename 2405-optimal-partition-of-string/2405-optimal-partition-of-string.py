class Solution:
    def partitionString(self, s: str) -> int:
        st = set()
        ans = 0
        for i in s:
            if i in st:
                st = {i}
                ans += 1
            else:
                st.add(i)
        return ans+1