# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingMHCD4A-YAE/
def solution(N, P, Q):
    # write your code in Python 3.6
    # make prime in range N
    prime_list = []
    for i in range(2, N // 2 + 1):
        isPrime = True
        for j in prime_list:
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            prime_list.append(i)

    # make semi prime
    semi_prime_idx = [False] * (N + 1)
    prime_length = len(prime_list)
    for i in range(prime_length):
        for j in range(i, prime_length):
            data = prime_list[i] * prime_list[j]
            if data <= N:
                semi_prime_idx[data] = True
            else:
                break

    # get count for semi prime
    semi_prime_cnt = [0] * (N + 1)
    for i in range(1, len(semi_prime_idx)):
        if semi_prime_idx[i]:
            semi_prime_cnt[i] = semi_prime_cnt[i - 1] + 1
        else:
            semi_prime_cnt[i] = semi_prime_cnt[i - 1]

    # get result
    M = len(P)
    result = [0] * M
    for i in range(M):
        result[i] = semi_prime_cnt[Q[i]] - semi_prime_cnt[P[i] - 1]
    
    return result
