class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = groupPrev
            
            # check if there is a full group of k nodes left
            count = 0
            while kth and count < k:
                kth = kth.next
                count += 1
           
            if not kth:
                break
            
            groupNext = kth.next
            
            # reverse the group
            # initialize prev to groupNext so the new tail connects to the rest of the list
            prev, curr = groupNext, groupPrev.next
            
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # identify the new tail to use for the next iteration
            new_group_tail = groupPrev.next
            
            # connect the previous part of the list to the new kth head
            groupPrev.next = kth
            groupPrev = new_group_tail
            
        return dummy.next