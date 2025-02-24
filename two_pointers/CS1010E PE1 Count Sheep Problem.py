# two pointers
s = "123456789101112131516172031" # expect 13
s = "123456789" # expect 9
s = "9123" # expect 0

# this is equivalent to 10^5 string length
s = ''.join([str(num) for num in range(1,25000)]) + "250001" # expect 25000

def count_sheep(s: str) -> int:

    # problem wants us to return the last correct count (i.e. last count that is contiguous)
    # this problem can be solved by tracking a next_to_match number and two-pointer

    # always start from 1
    next_to_match = str(1)

    # this second pointer represents the idx we are going to match for next_to_match
    curr_match_idx = 0
    for char in s:

        if char == next_to_match[curr_match_idx]:
            curr_match_idx += 1

            if curr_match_idx == len(next_to_match):
                next_to_match = str(int(next_to_match) + 1)
                curr_match_idx = 0 # reset

        else:
            return int(next_to_match)-1
        
    # no error trigger: alice counts correctly to sleep
    return int(next_to_match)-1 if curr_match_idx < len(next_to_match) else next_to_match

print(count_sheep(s))

s = "112358132021" # expect 13
s = "112358132134" # expect 34
s = "211" # expect 0
s = "12" # expect 1

def count_sheep_fib(s: str) -> int:

    # a variant of the above is that the sequence expected now is a fibonacci sequence
    # initialise two variables to track the next-to-match finbonacci number
    # s.t. next_fib = fib_prev2 + fib_prev1
    fib_prev2, fib_prev1 = 0, 1
    next_fib = str(fib_prev1 + fib_prev2)

    curr_match_idx = 0
    for idx, char in enumerate(s):

        if char == next_fib[curr_match_idx]:
            curr_match_idx += 1

            if curr_match_idx == len(next_fib):
                
                # update fib_prev
                fib_prev2, fib_prev1 = fib_prev1, int(next_fib)

                # handle the start of fibonacci seq.
                next_fib = str(fib_prev2 + fib_prev1) if idx > 0 else str(1)

                # reset match_idx
                curr_match_idx = 0 

        else:
            return fib_prev1 if fib_prev1 < int(next_fib) else fib_prev2
        
    # alice correctly spells out fibonacci seq.
    return fib_prev1 if curr_match_idx < len(next_fib) else next_fib

print(count_sheep_fib(s))