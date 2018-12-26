# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/training9S5CPH-2QF/
def solution(N):
    # write your code in Python 3.6
    A = int(N ** (1/2))
    count = 0
    for i in range(1, A + 1):
        if N % i == 0: # always increase 2 because of pair
            count += 2
    
    # check for square
    if A * A == N:
        count -= 1
    
    return count
