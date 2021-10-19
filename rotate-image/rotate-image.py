class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        visited = set()
        for i in range(n):
            for j in range(n):
                if str([i,j]) not in visited:
                    visited.add(str([i,j]))
                    yf=n-1-i
                    xf=j
                    visited.add(str([xf,yf]))
                    t = matrix[xf][yf]
                    matrix[xf][yf] = matrix[i][j]
                    matrix[i][j] = t