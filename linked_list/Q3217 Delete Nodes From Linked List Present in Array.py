# linked list - medium
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        # make nums a set
        num_set = set(nums)
        
        dummy_head = ListNode()
        # define a prev. node that is valid
        prev = dummy_head

        # iterate through the linked list and keep only valid nodes
        curr = head
        while True:

            if curr.val not in num_set:
                prev.next = ListNode(val=curr.val)
                prev = prev.next

            if not curr.next:
                break
            curr = curr.next

        return dummy_head.next
    
nums, head = [1,2,3], [1,2,3,4,5]
nums, head = [1], [1,2,1,2,1,2]
nums, head = [5], [1,2,3,4]
nums, head = [9,2,5], [2,10,9]