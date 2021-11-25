class TrieNode:
    def __init__(self): 
        self.children={} #handle duplicates and map chars to sub tries
        self.isWord=False #to mark a complete word
    
    def addWord(self,word):
        cur = self #set current pointer to self and iterate down adding any chars that previously didn't exist
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True #mark the last char as a word to indicate a complete word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie for each words
        trie = TrieNode()
        for w in words:
            trie.addWord(w)
        
        ROWS,COLS = len(board),len(board[0])
        
        res,visit = set(),set()
        
        def dfs(r,c,node,word):
            if r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visit or board[r][c] not in node.children: return
            
            visit.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.isWord: res.add(word)
                
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))
        
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] in trie.children: dfs(i,j,trie,'')
        
        return res