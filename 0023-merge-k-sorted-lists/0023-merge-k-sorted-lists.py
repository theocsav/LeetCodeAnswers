# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        
        # Push the head of each list into the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        dummy = ListNode()
        current = dummy
        
        # Extract min, add to result, and push next node
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
                
        return dummy.next