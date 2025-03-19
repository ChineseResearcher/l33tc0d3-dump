def sqrt(num, epsilon=0.001):

    # precision controls the size of increment
    precision, ans = 1, 0
    while abs(num - ans ** 2) > epsilon**2:
        
        base = 0
        while (ans + base * precision) ** 2 <= num:
            base += 1

        base -= 1
        # ans should be updated with the best approximation
        # at the current digit level specified by precision
        ans += base * precision
        # finer precision
        precision /= 10

    return ans

if __name__ == '__main__':

    num = 123456789
    print(f'sqrt finder: {sqrt(num)}')
    print(f'ground truth: {num ** 0.5}')