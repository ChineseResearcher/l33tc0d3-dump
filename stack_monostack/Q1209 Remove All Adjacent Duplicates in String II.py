# stack - medium
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # use a stack to keep track of occurrences of unique letters
        st = []

        for char in s:
            
            # no cancellation possible
            if not st or char != st[-1][0]:
                st.append([char, 1])
                
            else:
                st[-1][1] += 1
                if st[-1][1] == k:
                    st.pop()
                    
        return ''.join([char * freq for char, freq in st])
    
s, k = "abcd", 2
s, k = "deeedbbcccbdaa", 3
s, k = "pbbcggttciiippooaais", 2

Solution().removeDuplicates(s, k)