# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if list is empty or just one node
        if not head or not head.next:
            return head
        
        # traverse to get length and find the tail
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
            
        # huge k? just take the remainder
        k = k % length
        
        # if k is 0 (or multiple of length), list looks same
        if k == 0:
            return head
            
        # connect tail back to head
        tail.next = head
        
        # figure out where the new tail is
        # moving length - k spots gets us to the node right before the new head
        steps_to_new_tail = length - k
        new_tail = head
        
        # walk to the new tail
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
            
        # set the new head and break the ring
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head