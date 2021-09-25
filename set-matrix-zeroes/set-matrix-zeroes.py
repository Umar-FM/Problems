class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroCoordinates = []
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0: zeroCoordinates.append((r,c))

        for coord in zeroCoordinates:
            r,c = coord
            tr, tc = r,c

            while tr >= 0:
                matrix[tr][tc] = 0
                tr-=1
            tr, tc = r,c
            while tc >= 0:
                matrix[tr][tc] = 0
                tc-=1
            tr, tc = r,c
            while tr < len(matrix):
                matrix[tr][tc] = 0
                tr+=1
            tr, tc = r,c
            while tc < len(matrix[0]):
                matrix[tr][tc] = 0
                tc+=1
        
        