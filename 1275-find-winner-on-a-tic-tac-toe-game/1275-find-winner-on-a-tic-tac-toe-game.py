class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        arr = [["" for j in range(3)] for i in range(3)]
        for i, [x, y] in enumerate(moves):
            arr[x][y] = 'O' if i&1 else 'X'
        if arr[0][0] == arr[0][1] and arr[0][1] == arr[0][2] and arr[0][0]: return "A" if arr[0][0] == 'X' else 'B'
        if arr[0][0] == arr[1][1] and arr[1][1] == arr[2][2] and arr[0][0]: return "A" if arr[0][0] == 'X' else 'B'
        if arr[0][0] == arr[1][0] and arr[1][0] == arr[2][0] and arr[0][0]: return "A" if arr[0][0] == 'X' else 'B'
        if arr[0][1] == arr[1][1] and arr[1][1] == arr[2][1] and arr[0][1]: return "A" if arr[1][1] == 'X' else 'B'
        if arr[0][2] == arr[1][2] and arr[1][2] == arr[2][2] and arr[0][2]: return "A" if arr[0][2] == 'X' else 'B'
        if arr[0][2] == arr[1][1] and arr[1][1] == arr[2][0] and arr[0][2]: return "A" if arr[0][2] == 'X' else 'B'
        if arr[1][0] == arr[1][1] and arr[1][1] == arr[1][2] and arr[1][0]: return "A" if arr[1][2] == 'X' else 'B'
        if arr[2][0] == arr[2][1] and arr[2][1] == arr[2][2] and arr[2][0]: return "A" if arr[2][2] == 'X' else 'B'
        for i in range(3):
            for j in range(3):
                if arr[i][j] == "": return "Pending"
        return "Draw"