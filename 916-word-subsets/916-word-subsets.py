class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # have dict for storing number of chars needed
        d = {}
        for word in words2:
            # this is a temp dict to compare and store max chars in original dict 
            t = {}
            for i in word:
                #store number of times any char is coming in temp dict
                t[i] = t[i] + 1 if i in t else 1
            for i in t.keys():
                # here compare if new current word have more chars of any type, if yes then store that max to original dict
                d[i] = max(d[i], t[i]) if i in d else t[i]

        # have a array to store result
        arr = []
        # now lets start looping over words1 array
        for word in words1:
            # have new dict for every word in words1 to count its char counts
            di = {}
            is_there = True
            # count timings of chars in word
            for w in word:
                di[w] = di[w] + 1 if w in di else 1
            for i in d.keys():
                # check if required chars are present in current word if not then move to next word
                if i not in di or d[i] > di[i]:
                    is_there = False
                    break
            # if every char match add it to array
            if is_there:
                arr.append(word)
        return arr