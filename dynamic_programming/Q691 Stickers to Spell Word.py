from collections import Counter
from string import ascii_lowercase as lc

class Solution:
    def recursive_spell(self, currEnc, rFreq):

        r = ''.join([str(k) + str(rFreq[k]) for k in sorted(rFreq.keys())])
        # indicates all alphabets in target have been formed
        if currEnc == 0:
            return 0
        
        if (currEnc, r) in self.dp:
            return self.dp[(currEnc, r)]
        
        curr_res = float('inf')
        for i in range(self.N):

            common = currEnc & self.stickerEnc[i]
            if common != 0:
            
                nextEnc, ops = currEnc, []
                for j in range(26):
                    if common & (1 << j) != 0:

                        avail = self.stickerFreq[self.stickers[i]][lc[j]] 
                        decrement = min(rFreq[lc[j]], avail)

                        ops.append((j, decrement))

                        rFreq[lc[j]] -= decrement
                        if rFreq[lc[j]] == 0:
                            nextEnc &= ~(1 << j)

                curr_res = min(curr_res, 1 + \
                               self.recursive_spell(nextEnc, rFreq))
                
                # backtrack
                for j, decrement in ops:
                    rFreq[lc[j]] += decrement
                
        self.dp[(currEnc, r)] = curr_res
        return curr_res

    def minStickers(self, stickers, target):
        targetSet = set(target)
        # first confirm that target can be formed, i.e. no missing
        # alphabets in all stickers string that are part of target
        if targetSet - set(''.join(stickers)):
            return -1

        # create a alphebatical binary mapping
        alphaMap = {char:idx for idx, char in enumerate(lc)}

        # stickerFreq to store <wordStr, counter of alphabets>
        # stickerEnc to store alphabetical encoding of characters in a wordStr
        self.stickerFreq, self.stickerEnc = dict(), []
        for s in stickers:
            self.stickerFreq[s] = Counter(s)

            # encode
            bitmask = 0
            for k in self.stickerFreq[s].keys():
                bitmask |= (1 << alphaMap[k])

            self.stickerEnc.append(bitmask)

        # encode target as well
        targetEnc, targetFreq = 0, Counter(target)
        for char in targetSet:
            targetEnc |= (1 << alphaMap[char])

        self.N = len(stickers)
        self.dp = dict()
        self.stickers = stickers

        return self.recursive_spell(targetEnc, targetFreq)

stickers, target = ["with","example","science"], "thehat"
stickers, target = ["charge","mind","bottom"], "centorder"
stickers, target = ["travel","quotient","nose","wrote","any"], "lastwest"
stickers, target = ["xxxxy","xyyy"], "xxxxyyy"

Solution().minStickers(stickers, target)