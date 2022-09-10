class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        mat=[[0 for i in range(2*k+1)] for j in range(len(prices)+1)]
        for i in range(len(mat)-2,-1,-1):
            for j in range(2*k-1,-1,-1):
                if j%2==0:
                    mat[i][j]=max(mat[i+1][j+1]-prices[i],mat[i+1][j])
                else:
                    mat[i][j]=max(mat[i+1][j+1]+prices[i],mat[i+1][j])
        return mat[0][0]