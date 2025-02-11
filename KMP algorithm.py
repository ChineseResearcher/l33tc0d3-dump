# ver. 1
def kmp_matching(source:str, pattern:str) -> bool:

    # In KMP, total time complexity of O(n+m) where n is the length of source
    # and m is the length of the pattern, this is much faster than the naive O(n*m) approach
    n, m = len(source), len(pattern)

    # a critical operation is to construct a pie arr. when we process a pattern
    # the additional space of 1 is needed for us to correctly reference j pointer which
    # we should dial back to in the event of a mismatch between source[i] and pattern[j]
    pie = [0] * (m+1)

    # maintain a seen set
    seen = set()
    curr = 0
    for idx, char in enumerate(pattern):

        if char not in seen:
            curr = 0 # reset
            pie[idx+1] = curr

            seen.add(char)

        else:
            curr += 1
            pie[idx+1] = curr

    # one-pass check through source, with second pointer j associated with pattern
    j = 0
    for i in range(n):
        
        if source[i] == pattern[j]:
            j += 1

            # full pattern matched
            if j == m:
                return True

        # need to dial back j pointer 
        else:
            # in worst case j goes back to zero
            while j > 0:

                j = pie[j]
                if source[i] == pattern[j]:
                    j += 1
                    break

            # print(f'dial back j to {j}')

    return False

# ver. 2
def kmp_matching(source:str, pattern:str) -> bool:

    def kmp_prefix(pattern):
        # the prefix arr. tells us that if pref[i] = k (possibly 0), 
        # then pattern[:(i+1)] contains a prefix of length k that is also suffix
        # e.g. pattern "abba" would yield prefix arr. [0,0,1,2]
        # at i=3, pref[i] = 2, meaning for pattern[:(3+1)] (essentially "abba")
        # the longest prefix that is also suffix is of length 2 -> "ab"

        pref, k = [0], 0

        for i in range(1, len(pattern)):

            # if no match
            while k > 0 and pattern[k] != pattern[i]:
                # print(f'pattern[k={k}]: {pattern[k]} != pattern[i={i}]: {pattern[i]}')
                # print(f'reassign k to {pref[k-1]}')
                # worst case k gets reduce to 0, exit while loop
                k = pref[k-1]

            # if match
            if pattern[k] == pattern[i]:
                # print(f'increment k to {k+1} for matching')
                k += 1

            pref.append(k)

        return pref

    pref = kmp_prefix(pattern)

    # k represents the matchedIdx
    k = 0
    for char in source:

        while k > 0 and pattern[k] != char:
            k = pref[k-1]

        if pattern[k] == char:
            k += 1

        if k == len(pattern):
            return True
        
    return False

source = "ababcabcabababd"
pattern = "ababd"

source = "aaaaaaaaab"
pattern = "aaab"

source = "hello"
pattern = "ll"

source = "aaaaa"
pattern = "bba"

source = "aaabaaabaaa"
pattern = "aaabaaa"

source = "ababcabcabababd"
pattern = "ababcab"

source = "abc"
pattern = "abcd"

# exploring worst case:
source = "a"*int(1e5) + "b"
pattern = "a"*int(5e4) + "b"

kmp_matching(source, pattern)