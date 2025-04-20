# heap - hard
import heapq
class Solution:
    def smallestRange(self, nums):
        # The challenging parts to this problem are:
        # 1) conceptualising a min-heap to always be comparing the root (smallest) elements of every sub-list
        # 2) handling the iteration of next element for an already popped element in O(1) time
        # to achieve 2), our heap stores a 3rd dimensional element called element index
        
        # Min heap to store the first element from each list along with its index in the list
        min_heap = []
        curr_max = float('-inf')
        
        # Initialize the heap with the first element from each list
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))  # (value, list index, element index)
            curr_max = max(curr_max, nums[i][0])
        
        # To store the smallest range
        ans = [float('-inf'), float('inf')]
        
        # Continue processing until one list is exhausted
        while min_heap:
            curr_min, list_idx, elem_idx = heapq.heappop(min_heap)
            
            # Update the result if the current range is smaller
            # Note: as we processed the already sorted (ordered in ascending) sublists, we naturally
            # avoid having to handle a tie situation of two equal ranges
            if curr_max - curr_min < ans[1] - ans[0]:
                ans = [curr_min, curr_max]
            
            # If we've reached the end of the list, break
            # Why? We want to ensure our range covers all lists, so if any list is already exhausted
            # We simply return the best interval so far
            if elem_idx + 1 == len(nums[list_idx]):
                break
            
            # Add the next element of the current list to the heap
            next_elem = nums[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_elem, list_idx, elem_idx + 1))
            curr_max = max(curr_max, next_elem)  # Update the max element

        return ans
    
nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
nums = [[1,2,3],[1,2,3],[1,2,3]]

Solution().smallestRange(nums)