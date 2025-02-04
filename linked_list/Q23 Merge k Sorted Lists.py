# linked list - hard
import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        # first start by pushing all the first elements of ll_list into a min heap
        min_heap = []

        node_id = 0
        for ll in lists:
            if ll is not None:
                heapq.heappush(min_heap, (ll.val, node_id, ll))
                node_id += 1

        # create a dummy ll head
        ans = ListNode()

        curr = ans
        while min_heap:

            _, _, node = heapq.heappop(min_heap)
            # initiate merging with the next smallest node
            curr.next = node

            node_id += 1
            # we also want to push the next node of the popped node into heap
            if node.next: heapq.heappush(min_heap, (node.next.val, node_id, node.next))

            # move the ans pointer to the next node
            curr = curr.next

        return ans.next
    
# helpers
def print_linked_list(head):
    current = head
    sequence = []
    
    while current is not None:
        sequence.append(current.val)
        current = current.next
        
    print(sequence)
        
    
def create_linked_list(python_list):
    # If the input list is empty, return None
    if not python_list:
        return None
    
    # Create the head node
    head = ListNode(python_list[0])
    current = head
    
    # Iterate through the rest of the elements in the list and create nodes
    for value in python_list[1:]:
        current.next = ListNode(value)
        current = current.next
    
    return head

lists = [[]]
lists = []
lists = [[1,4,5],[1,3,4],[2,6]]

ll_list = [create_linked_list(l) for l in lists]
print_linked_list(Solution().mergeKLists(ll_list))

