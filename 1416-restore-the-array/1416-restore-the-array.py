class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        # initialize memory: we have only one possibility 
        #   to choose a sequence with zero length
        d = {0: 1}

        for i in range(1, len(s) + 1):
            # keep memory up-to-date: filter out values 
            #   outside [1; k] range
            d = {j: d[j] for j in d if 1 <= int(s[j:i]) <= k}

            # update memory with i-th value: each element of d 
            #   form a sequence that ends with the i-th character
            d[i] = sum(d.values()) % 1000000007

        return d[len(s)]
