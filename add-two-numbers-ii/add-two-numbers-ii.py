# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1,l2):
        len1 = self.getLength(l1)
        len2 = self.getLength(l2)
        
        if len1<len2: l1=self.padLL(l1,len2-len1)
        if len2<len1: l2=self.padLL(l2,len1-len2)
        s= self.addLL(l1,l2)
        if s.val//10:
            s=ListNode(s.val//10,s)
            s.next.val = s.next.val%10
        return s
    
    def addLL(self,l1,l2):
        if not l1.next: return ListNode(l1.val+l2.val)
        nextSum = self.addLL(l1.next,l2.next)
        carry=nextSum.val//10
        nextSum.val = nextSum.val%10
        return ListNode(l1.val+l2.val+carry,nextSum)
            
        
    
    def getLength(self,LL,l=1):
        while LL.next:
            LL=LL.next
            l+=1
        return l
    
    def padLL(self,LL,n):
        head=ListNode()
        p=head
        for _ in range(n-1):
            p.next=ListNode()
            p=p.next
        p.next=LL
        return head