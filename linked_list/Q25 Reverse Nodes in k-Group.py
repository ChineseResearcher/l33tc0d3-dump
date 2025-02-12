# linked list - hard

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        new_head, new_tail = dict(), dict()
        node_idx, curr_grp = 0, []

        curr = head
        while True:

            curr_grp.append(curr)
            curr = curr.next if curr.next else None

            # once a group is fully subscribed
            # reverse the links in this group
            if len(curr_grp) == k:

                # assign new head/tail considering reversed links
                new_head[node_idx // k] = curr_grp[-1]
                new_tail[node_idx // k] = curr_grp[0]
                
                # reverse links operations:
                while curr_grp:
                    
                    # first sever the link: prev -> curr
                    # then create the link: curr -> prev
                    if len(curr_grp) > 1:  
                        curr_grp[-2].next = None
                        curr_grp[-1].next = curr_grp[-2]

                    curr_grp.pop()
        
            if curr is None: break
            node_idx += 1

        # ref. the last updated node_idx
        for grp in range((node_idx + 1) // k - 1):
            new_tail[grp].next = new_head[grp+1]

        # collect the nodes that have not reversed
        if curr_grp:
            new_tail[(node_idx + 1) // k - 1].next = curr_grp[0]

        return new_head[0]
    
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

head, k = [1,2,3,4,5], 2
head, k = [1,2,3,4,5], 3
head, k = [1,2,3,4,5,6,7], 3

head = create_linked_list(head)
print_linked_list(Solution().reverseKGroup(head, k))
    
