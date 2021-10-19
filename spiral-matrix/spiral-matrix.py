class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        visited = set()
        n = len(matrix)
        m = len(matrix[0])
        i=0
        j=0
        total = 0
        
        while total < (m*n):
            while j<m and str([i,j]) not in visited:
                res.append(matrix[i][j])
                visited.add(str([i,j]))
                total += 1
                j+=1
            j-=1
            i+=1
            while i<n and str([i,j]) not in visited:
                res.append(matrix[i][j])
                visited.add(str([i,j]))
                total += 1
                i+=1
            i-=1
            j-=1
            while j>=0 and str([i,j]) not in visited:
                res.append(matrix[i][j])
                visited.add(str([i,j]))
                total += 1
                j-=1
            j+=1
            i-=1
            while i>=0 and str([i,j]) not in visited:
                res.append(matrix[i][j])
                visited.add(str([i,j]))
                total += 1
                i-=1
            i+=1
            j+=1
        return res