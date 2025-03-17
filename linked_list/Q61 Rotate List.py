# linked list - medium
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head: return None

        # traverse the linked list and record their node vals
        vals = []

        curr = head
        while True:

            vals.append(curr.val)
            if not curr.next:
                break

            curr = curr.next

        # modulo k such that we get the correct right shifts
        k %= len(vals)
        # rotate the values according to k
        vals = vals[-k:] + vals[:len(vals)-k]

        # assign the rotated values
        idx = 0
        curr = head
        while True:

            curr.val = vals[idx]
            if not curr.next:
                break

            idx += 1
            curr = curr.next

        return head

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

# TC
head, k = [1,2,3,4,5], 2
head, k = [0,1,2], 4

ll = create_linked_list(head)
print_linked_list(Solution().rotateRight(ll, k))