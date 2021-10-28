class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def recurse(i,j,board,word,visited):
            if not word: return True
            if i<0 or i>=len(board): return False
            if j<0 or j>=len(board[0]): return False
            if (i,j) in visited: return False
            if board[i][j] != word[0]: return False
            
            visited.add((i,j))
            
            res=False
            res = res or recurse(i+1,j,board,word[1:],visited)
            res = res or recurse(i-1,j,board,word[1:],visited)
            res = res or recurse(i,j+1,board,word[1:],visited)
            res = res or recurse(i,j-1,board,word[1:],visited)
            visited.remove((i,j)) #remove this because no options were viable so backtrack so that if another route comes then this is no ignored
            return res
            
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    res = recurse(i,j,board,word,set())
                    if res: return True
        return False
        