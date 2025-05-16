# dp - medium
class Solution:
    def knightDialer(self, n: int) -> int:
        # since we only have 10 dial numbers, the transition matrix size is of 10 by 10
        T = [ [0] * 10 for _ in range(10) ]

        # notice that from the perspective of any dial number,
        # there can be up to 3 previous dial numbers that it could have transitioned from
        # e.g. 0 transitioned from 4 & 6

        # hardcode the transitions by observation
        # Note: number 5 is a dead end
        T[0][4], T[0][6] = 1, 1
        T[1][6], T[1][8] = 1, 1
        T[2][7], T[2][9] = 1, 1
        T[3][4], T[3][8] = 1, 1
        T[4][0], T[4][3], T[4][9] = 1, 1, 1
        T[6][0], T[6][1], T[6][7] = 1, 1, 1
        T[7][2], T[7][6] = 1, 1
        T[8][1], T[8][3] = 1, 1
        T[9][2], T[9][4] = 1, 1

        ### helpers for linear algebra ###
        MOD = int(1e9 + 7)
        # multiplication of matrix
        def mat_mult(A, B):
            # A, B are N×N
            N = len(A)

            C = [[0] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    s = 0
                    for k in range(N):
                        s += (A[i][k] * B[k][j]) % MOD
                    C[i][j] = s

            return C

        # multiplication of vector and matrix
        def mat_vec_mult(A, x):
            # A is N × N, x is 1 x N
            N = len(A)

            y = [0] * N
            for i in range(N):
                s = 0
                for j in range(N):
                    s += (A[i][j] * x[j]) % MOD
                y[i] = s

            return y

        # fast exponentiation of matrix
        def mat_pow(T, k):
            # Compute T^k in O(N^3 log k)
            # Start with identity matrix
            N = len(T)
            result = [[1 if i == j else 0 for j in range(N)] for i in range(N)]

            base = T
            while k > 0:
                if k & 1:
                    result = mat_mult(result, base)
                base = mat_mult(base, base)
                k >>= 1

            return result

        ### computing results using helpers ###

        T_power_k = mat_pow(T, n-1)
        # we can start from any number cells
        x = [1] * 10
        final_freq = mat_vec_mult(T_power_k, x)

        return sum(final_freq) % MOD
    
n = 1 # no moves, just 10 distinct seq. as we have 10 starting pos.
n = 2
n = 3131

Solution().knightDialer(n)