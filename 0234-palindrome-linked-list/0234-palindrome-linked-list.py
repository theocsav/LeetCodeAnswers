# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # makin a list to hold values
        vals = []
        curr = head
        
        # loopin thru the linked list
        while curr:
            vals.append(curr.val)
            # movin to da next node
            curr = curr.next
            
        # ez check: is list same as its reverse?
        return vals == vals[::-1]