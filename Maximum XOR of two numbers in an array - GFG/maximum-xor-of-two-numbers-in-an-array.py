#User function Template for python3
class TrieNode :
    def __init__(self):
        self.children = {}

class Trie :
    def __init__(self) :
        self.root = TrieNode()

    def insert(self, n) :
        temp = self.root
        i = 31
        while i >= 0 :
            bit = (n >> i) & 1
            if bit not in temp.children: 
                temp.children[bit] = TrieNode()
            temp = temp.children[bit]
            i -= 1

    def max_xor_helper(self, value) :
        temp = self.root
        current_ans = 0
        i = 31
        while i >= 0:
            bit = (value >> i) & 1
            if bit^1 in temp.children:
                temp = temp.children[bit^1]
                current_ans += (1 << i)
            else:
                temp = temp.children[bit]
            i -= 1
        return current_ans

class Solution:
    def max_xor(self, arr, n):
        #code here
        trie = Trie()
        max_val = 0
        trie.insert(arr[0])
        for num in arr[1:]:
            max_val = max(trie.max_xor_helper(num),max_val)
            trie.insert(num)
        return max_val



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		arr = list(map(int,input().split()))
		ob = Solution();
		print(ob.max_xor(arr,n))
	
# } Driver Code Ends