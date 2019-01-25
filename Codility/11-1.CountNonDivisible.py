# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingNFVDM5-SZC/
def solution(A):
    # write your code in Python 3.6
    N = len(A)
    count_list = [0] * (2 * N + 1)
    for data in A:
        count_list[data] += 1
    
    result = [0] * N
    saved = [-1] * (2 * N + 1)
    for j in range(N):
        current = A[j]
        # if current == 1, all others are non divisible
        # saved != -1, already calculated value
        # else, calculate
        if current == 1:
            result[j] = N - count_list[1]
        elif saved[current] != -1:
            result[j] = saved[current]
        else:
            count = 0
            # sqrt(current) is enough for calculation
            for i in range(1, int(current ** 0.5) + 1):
                if current % i == 0:
                    count += count_list[i]
                    if i != current // i:
                        count += count_list[current // i]
                    
            result[j] = N - count
            saved[current] = result[j]
    
    return result
