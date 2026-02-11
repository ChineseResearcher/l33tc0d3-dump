# segment tree - hard
from typing import List
class SegmentTree:
    def __init__(self, n):
        self.n = n
        suit_len = 2 << self.n.bit_length()
        # 维护区间内的最小值
        self.tree_min = [0] * suit_len
        # 维护区间内的最大值
        self.tree_max = [0] * suit_len
        # 懒惰标记，用于区间加法
        self.lazy = [0] * suit_len

    # 向下传递懒惰标记
    def push_down(self, node):
        if self.lazy[node] != 0:
            add_val = self.lazy[node]
            left = node * 2
            right = node * 2 + 1
            
            # 更新左子节点
            self.lazy[left] += add_val
            self.tree_min[left] += add_val
            self.tree_max[left] += add_val
            
            # 更新右子节点
            self.lazy[right] += add_val
            self.tree_min[right] += add_val
            self.tree_max[right] += add_val
            
            # 清除当前节点的标记
            self.lazy[node] = 0

    # 向上更新节点信息
    def push_up(self, node):
        # 当前区间的最小/最大值来源于左右子树
        self.tree_min[node] = min(self.tree_min[node * 2], self.tree_min[node * 2 + 1])
        self.tree_max[node] = max(self.tree_max[node * 2], self.tree_max[node * 2 + 1])

    # 区间更新：将 [l, r] 范围内的值全部加上 val
    def update(self, node, start, end, l, r, val):
        # 区间不重叠，直接返回
        if l > end or r < start:
            return
        
        # 当前区间完全包含在更新范围内
        if l <= start and end <= r:
            self.tree_min[node] += val
            self.tree_max[node] += val
            self.lazy[node] += val
            return
        
        # 否则下放标记，递归更新子节点
        self.push_down(node)
        mid = (start + end) // 2
        self.update(node * 2, start, mid, l, r, val)
        self.update(node * 2 + 1, mid + 1, end, l, r, val)
        
        # 子节点更新完后，更新当前节点
        self.push_up(node)

    # 寻找区间 [l, r] 内 最左边 的值为 0 的位置
    def find_first_zero(self, node, start, end, l, r):
        # 当前区间的最小值 > 0 或 最大值 < 0，不可能有 0
        if self.tree_min[node] > 0 or self.tree_max[node] < 0:
            return -1
        
        # 范围越界
        if l > end or r < start:
            return -1
            
        # 叶子
        if start == end:
            return start if self.tree_min[node] == 0 else -1
        
        # 下放标记
        self.push_down(node)
        mid = (start + end) // 2
        
        # 贪心，优先查左子树，因为我们要找最左边的下标 L
        res = self.find_first_zero(node * 2, start, mid, l, r)
        if res != -1:
            return res
        # 左边没找到，查右边
        return self.find_first_zero(node * 2 + 1, mid + 1, end, l, r)

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
            
        # 记录每个数字上一次出现的位置
        last_pos = {}  # 值->下标
        prev_occur = [-1] * n  # 下标->下标
        
        for i, x in enumerate(nums):
            if x in last_pos:
                prev_occur[i] = last_pos[x]
            last_pos[x] = i
            
        # 初始化线段树
        st = SegmentTree(n)
        ans = 0
        
        # 移动右端点 R
        for R in range(n):
            val = nums[R]
            
            # 偶数平衡差 +1，奇数平衡差 -1
            change = 1 if val % 2 == 0 else -1
            
            # 新元素 nums[R] 只对起始点 L 位于 (prev_occur[R], R] 之间的子数组是"新"的
            update_l = prev_occur[R] + 1
            update_r = R
            
            # 区间全部加上 change
            st.update(1, 0, n - 1, update_l, update_r, change)
            
            # 在 [0, R] 范围内找最左边的 0
            # 找到一个 L，使得子数组 nums[L...R] 的平衡差为 0
            target_l = st.find_first_zero(1, 0, n - 1, 0, R)
            
            if target_l != -1:
                # 找到，计算长度
                cur_len = R - target_l + 1
                if cur_len > ans:
                    ans = cur_len
                    
        return ans

nums = [2,5,4,3]
nums = [1,2,3,2]
nums = [3,2,2,5,4]
nums = [1] * int(1e5)

Solution().longestBalanced(nums)