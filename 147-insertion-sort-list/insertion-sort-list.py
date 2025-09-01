# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        dummy=ListNode(0)
        while current:
            prev=dummy
            next_temp=current.next
            while prev.next and prev.next.val<current.val:
                prev=prev.next
            current.next=prev.next
            prev.next=current
            current=next_temp
        return dummy.next
        