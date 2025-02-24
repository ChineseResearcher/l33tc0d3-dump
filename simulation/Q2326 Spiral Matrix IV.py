# simulation - medium
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def spiralMatrix(self, m, n, head):
        grid = [[-1] * n for _ in range(m)]
        m, n = len(grid), len(grid[0])

        mIter, nIter = m-1, n
        # 0: right, 1: down, 2: left, 3: up
        direction = 0 
        rowPos, colPos = 0, -1

        # define the start of the ll
        currNode = head
        
        grid_visited = 0
        while grid_visited < m * n:

            if direction in [0, 2]:
                for i in range(1, nIter+1):
                    if currNode == None:
                        return grid
                    grid[rowPos][colPos+i if direction == 0 else colPos-i] = currNode.val
                    grid_visited += 1
                    currNode = currNode.next
                colPos = colPos + nIter if direction == 0 else colPos - nIter
                nIter -= 1

            if direction in [1, 3]:
                for i in range(1, mIter+1):
                    if currNode == None:
                        return grid
                    grid[rowPos+i if direction == 1 else rowPos-i][colPos] = currNode.val
                    grid_visited += 1
                    currNode = currNode.next
                rowPos = rowPos + mIter if direction == 1 else rowPos - mIter
                mIter -= 1

            direction = (direction + 1) % 4
            # print(f'updating coordinate to {rowPos}, {colPos}')

        return grid
    
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

# testcases
m, n, head = 3, 5, create_linked_list([3,0,2,6,8,1,7,9,4,2,5,5,0])
m, n, head = 1, 4, create_linked_list([0,1,2])

Solution().spiralMatrix(m, n, head)