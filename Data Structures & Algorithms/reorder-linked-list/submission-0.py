# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dequeue = []
        
        cur = head
        while cur:
            dequeue.append(cur.val)
            cur = cur.next
        
        newNode = ListNode()

        cur = newNode

        i, j = 0, len(dequeue) - 1
        while i < j:
            #print(f"{dequeue[i]}, {dequeue[j]}")
            nodei = ListNode(dequeue[i])
            nodej = ListNode(dequeue[j])
            cur.next = nodei
            nodei.next = nodej
            cur = nodej
            i += 1
            j -= 1
        
        if i == j:
            nodei = ListNode(dequeue[i])
            cur.next = nodei
        
        head.val = newNode.next.val
        head.next = newNode.next.next
            


