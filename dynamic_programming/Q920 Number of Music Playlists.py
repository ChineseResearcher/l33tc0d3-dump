# dp - hard
from functools import cache
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        
        # core ideas:
        # 1) we want to recursively add songs to our playlist until the size
        # of playlist reaches "goal"

        # 2) at each recursive step, when adding a song, it could be a new song
        # (i.e. unplayed before) or an old song (i.e. played before)

        # 3) the key problem is how do we know if we could play an old song at the
        # curr. step and if yes, how many of such old songs can we play?

        # 4) to tackle (3), we keep a state "oldSong" tracking 
        # the UNIQUE / DISTINCT cnt of songs already played

        MOD = int(1e9 + 7)

        @cache
        def recursive_add(currGoal, oldSongCnt):

            if currGoal == 0:
                # make sure when we have built a playlist of size "goal"
                # it contains exactly n unique songs as desired
                return 1 if oldSongCnt == n else 0
            
            # we have n-oldSongCnt of songs left unplayed, which can be added as a new song
            play_new = (n-oldSongCnt) * recursive_add(currGoal-1, oldSongCnt+1) % MOD
            # the problem requires s.t. when a old song is to be played
            # at least k other unique songs have been played
            # in other words, for a song to be repeated, k other unique songs would need
            # to be played in between this repeating song
            play_old = 0
            if oldSongCnt > k:
                play_old = (oldSongCnt-k) * recursive_add(currGoal-1, oldSongCnt) % MOD

            return (play_new + play_old) % MOD

        return recursive_add(goal, 0)
    
n, goal, k = 2, 3, 0
n, goal, k = 2, 3, 1
n, goal, k = 50, 100, 20

Solution().numMusicPlaylists(n, goal, k)