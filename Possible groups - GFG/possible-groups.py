from collections import Counter
#User function Template for python3

class Solution:
    def findgroups(self, arr, n):
        # code here
        d = Counter([i%3 for i in arr])
        return (d[0] * (d[0]-1)) // 2 + (d[1] * d[2]) + (d[0] * (d[0] - 1) * (d[0] - 2)) // 6 + (d[1] * (d[1] - 1) * (d[1] - 2)) // 6 + (d[2] * (d[2] - 1) * (d[2] - 2)) // 6 + d[0] * d[1] * d[2]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findgroups(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends