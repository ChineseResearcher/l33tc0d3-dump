# prefix sum - medium
class Solution:
    def minOperations(self, boxes):
        # initiate two variables
        # 1) one_box tracking the total count of '1' box in the given string
        # 2) curr_moves is initiated to the case where all balls need to be moved to first box
        one_box, curr_moves = 0, 0
        for idx, box in enumerate(boxes):

            if box == '1':
                one_box += 1
                curr_moves += idx
                
        # for every '1' box encountered, increment the variable seen
        seen = 0
        ans = []
        for idx, box in enumerate(boxes):

            ans.append(curr_moves)

            # update seen
            if box == '1':
                seen += 1

            # update curr_moves according to seen & not seen
            # the "not seen" part is derived from two prefix sums: one_box & seen

            # curr_moves decrements by the number of one boxes to the right
            # why? imagine by moving one unit rightwards, if there are k one boxes
            # to the right, then the moves needed to bring all to them to the curr. pos reduces by k
            curr_moves -= (one_box - seen)
            # similar reasoning for seen one boxes moving to the left, distance gets incremented
            # as we are moving further away from them
            curr_moves += seen

        return ans
    
boxes = "110"
boxes = "001011"
boxes = "010101010"

Solution().minOperations(boxes)