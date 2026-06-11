# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        i = head
        j = i.next
        while i.next and j.next and j.next.next:
            if i == j:
                return True
            if i.next:
                i = i.next
            if j.next.next:
                j = j.next.next
        return False
