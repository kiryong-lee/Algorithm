# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingKGDNZV-WZQ/
def solution(K, A):
    # write your code in Python 3.6
    
    result = 0
    length = 0
    for rope in A:
        if rope >= K:
            result += 1
            length = 0
        else:
            length += rope
            if length >= K:
                result += 1
                length = 0
            
    return result
