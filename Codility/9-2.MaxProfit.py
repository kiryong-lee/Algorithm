# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingVJ942E-49T/
def solution(A):
    # write your code in Python 3.6
    if len(A) < 2:
        return 0
    
    _max = 0
    min_data = A.pop(0)
    for data in A:
        current = data - min_data
        if current > 0:
            # if max value is smaller than current, then change max value
            if _max < current:
                _max = current
        # if current value is negative, then change min_data
        else:
            min_data = data
    
    return _max
