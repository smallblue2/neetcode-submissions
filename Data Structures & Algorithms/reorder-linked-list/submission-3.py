# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Find midpoint
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        midpoint = slow

        prev = None
        cur = midpoint.next
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        midpoint.next = None

        """
        1,2,3
        5,4

        itmp = 2
        jtmp = 4
        1 -> 5 -> 2 ->
        """

        i, j = head, prev
        while j:
            itmp = i.next
            jtmp = j.next
            i.next = j
            j.next = itmp
            i = itmp
            j = jtmp

            
