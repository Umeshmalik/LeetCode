class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        total_words_len = word_len * len(words)
        d = collections.Counter(words)
        ans = []
        for i in range(0, len(s) - total_words_len+1):
            str_cut = s[i : i+total_words_len]
            arr = []
            for j in range(0, len(str_cut), word_len):
                arr.append(str_cut[j : j + word_len])
            if collections.Counter(arr) == d:
                ans.append(i)
        return ans