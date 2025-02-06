# linked list - medium

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head):
        # obtaining the next-greater element is a direct application of monotonic stack
        ans = []

        # a monoDesc stack to store the indices of elements which have desc. val
        idxStack = []

        curr, currIdx = head, 0
        while True:

            currVal = curr.val
            # expand ans: default to 0
            ans.append(0)

            while idxStack and currVal > idxStack[-1][0]:
                _, idx = idxStack.pop()
                # assign next greater
                ans[idx] = currVal

            idxStack.append([currVal, currIdx])
            if not curr.next: break

            curr = curr.next
            currIdx += 1

        return ans
    
# helper
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

head = [2,1,5]
head = [2,7,4,3,5]

Solution().nextLargerNodes(create_linked_list(head))

