# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        leftToRight=False #will be false because will be right to left for second level
        ans=[]
        q=collections.deque()
        q.append(root)
        
        while q:
            local=[]
            q.reverse()
            for i in range(len(q)):
                node = q.popleft()
                local.append(node.val)
                if leftToRight:
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                else:
                    if node.right: q.append(node.right)
                    if node.left: q.append(node.left)
            
            local.reverse()
            ans.append(local)
            leftToRight= not leftToRight
        
        return ans