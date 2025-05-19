# dp - hard
class Solution:
    def numOfWays(self, n: int) -> int:
        
        MOD = int(1e9 + 7)
        # we can definitely re-use the solution to Q1931 for this question
        # but since there are only three columns, it allows us to capture some transitions relationships

        # imagine there's only two kinds of tiling schemes
        # 1) three-color tiling (e.g. R/G/Y, R/Y/G, ...)
        # 2) two-color tiling (e.g. R/Y/R, ...)
        # by drawing out the transitions, we can derive the following summarisation
        T = [ [2, 2], [2, 3] ]

        # as given in the question, we can see 12 tilings possible
        # for n = 1, of which 6 belongs to group (1), and another 6 belongs to (2)
        x = [6, 6]

        ### helpers for linear algebra ###

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
        final_freq = mat_vec_mult(T_power_k, x)

        return sum(final_freq) % MOD
    
n = 1
n = 5000

Solution().numOfWays(n)