# dp - hard
class Solution:
    def checkRecord(self, n: int) -> int:
        
        # we have six (eligible) states, so the transition matrix is 6 by 6
        # e.g. (A0, L0) means total absence count is 0, current consecutive late days is 1
        # (A1, L2) means total absence count is 1, current consecutive late days is 2
        # the states are in the order: (A0, LO), (A0, L1), (A0, L2),
        #                              (A1, L0), (A1, L1), (A1, L2)
        T = [ [0] * 6 for _ in range(6) ]

        # hardcode the transitions by deductions

        # (A0, L0) -> (A0, L0): pick "Present"
        T[0][0] = 1
        # (A0, L0) -> (A0, L1): pick "Late"
        T[1][0] = 1
        # (A0, L0) -> (A1, L0): pick "Absence"
        T[3][0] = 1
        # (A0, L1) -> (A0, L0): pick "Present"
        T[0][1] = 1
        # (A0, L1) -> (A0, L2): pick "Late"
        T[2][1] = 1
        # (A0, L1) -> (A1, L0): pick "Absence"
        T[3][1] = 1
        # (A0, L2) -> (A0, L0): pick "Present"
        T[0][2] = 1
        # (A0, L2) -> (A1, L0): pick "Absence"
        T[3][2] = 1
        # (A1, L0) -> (A1, L0): pick "Present"
        T[3][3] = 1
        # (A1, L0) -> (A1, L1): pick "Late"
        T[4][3] = 1
        # (A1, L1) -> (A1, L0): pick "Present"
        T[3][4] = 1
        # (A1, L1) -> (A1, L2): pick "Late"
        T[5][4] = 1
        # (A1, L2) -> (A1, L0): pick "Present"
        T[3][5] = 1

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

        # we start from "Present", "Late" or "Absence"
        x = [1,1,0,1,0,0]
        final_freq = mat_vec_mult(T_power_k, x)

        return sum(final_freq) % MOD

n = 1
n = 2
n = 10101

Solution().checkRecord(n)