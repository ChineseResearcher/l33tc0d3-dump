# binary search - hard

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        MA = mountainArr

        n = MA.length()
        # key ideas:
        # 1) we are given a mountain arr, so for any index we will be
        #    a) on the ascending side
        #    b) on the descending side
        #    c) at the mountain top

        # 2) make use of binary search to:
        #    a) first find the mountain top index
        #    b) then find if target exist in [0...top], if not [top...n]

        # task (1): find mountain top
        l, r = 0, n-1
        while l <= r:

            mid = (l + r) // 2

            curr = MA.get(mid)
            to_left = MA.get(mid-1) if mid-1 >= 0 else -1
            to_right = MA.get(mid+1) if mid+1 < n else -1

            if curr > to_left and curr > to_right:
                if curr == target:
                    return mid
                    
                top = mid
                break
            elif to_left < curr < to_right:
                l = mid + 1
            elif to_left > curr > to_right:
                r = mid - 1

        # task (2)(a): find target in range [0...top]
        l, r = 0, top-1
        while l <= r:

            mid = (l + r) // 2
            curr = MA.get(mid)

            if curr == target:
                return mid
            elif curr < target:
                l = mid + 1
            elif curr > target:
                r = mid - 1

        # task (2)(b): find target in range [top...n]
        l, r = top+1, n-1
        while l <= r:

            mid = (l + r) // 2
            curr = MA.get(mid)

            if curr == target:
                return mid
            elif curr < target:
                r = mid - 1
            elif curr > target:
                l = mid + 1

        return -1

mountainArr, target = [1,2,3,4,5,3,1], 3
mountainArr, target = [0,1,2,4,2,1], 3
mountainArr, target = [1,5,2], 5