# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        vals=[]
        while current:
            vals.append(current.val)
            current=current.next
        ans=[]
        maxval=float('-inf')
        for i in range(len(vals)-1,-1,-1):
            if vals[i]>=maxval:
                ans.append(vals[i])
                maxval=vals[i]
        ans.reverse()
        dummy=ListNode(0)
        prev=dummy
        for v in ans:
            node=ListNode(v)
            prev.next=node
            prev=node
        return dummy.next


