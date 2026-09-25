# sorting - medium
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        n = len(strs)
        # key ideas:
        # 1) anagrams reduce to the same form when sorted
        # 2) sort the strs array first by the length of each string, and by alphabets
        mstrs = [(''.join(sorted(x)), i) for i, x in enumerate(strs)]
        mstrs.sort(key=lambda x: (len(x[0]), x[0]))

        ans, curr_grp = [], [strs[mstrs[0][1]]]
        for i in range(1, n):
            x, j = mstrs[i]
            
            if len(x) > len(mstrs[i - 1][0]):
                ans.append(curr_grp)
                curr_grp = [strs[j]]
                continue

            if x != mstrs[i - 1][0]:
                ans.append(curr_grp)
                curr_grp = [strs[j]]
                continue

            curr_grp.append(strs[j])

        # collect last group
        ans.append(curr_grp)

        return ans

strs = [""]
strs = ["a"]
strs = ["eat","tea","tan","ate","nat","bat"]

Solution().groupAnagrams(strs)
