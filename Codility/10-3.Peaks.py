# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingUZQEFJ-NP6/
def solution(A):
    # write your code in Python 3.6
    N = len(A)
    # make peaks
    peaks = []
    for i in range(1, N - 1):
        if A[i - 1] < A[i] > A[i + 1]:
            peaks.append(i)

    # get block
    result = 0
    for i in range(1, len(peaks) + 1):
        if N % i == 0:
            block_size = N // i
            block_start = 0
            block_end = block_size
            count = 0
            for p in peaks:
                if block_start <= p < block_end:
                    count += 1
                    block_start += block_size
                    block_end += block_size
                    if count == i:
                        result = i
                        break
                elif p >= block_end:
                    break

    return result
