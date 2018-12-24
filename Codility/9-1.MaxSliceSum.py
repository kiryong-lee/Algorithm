# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingY2YANN-8DH/
def solution(A):
    # write your code in Python 3.6
    _max = A[0]
    _current = A.pop(0)
    for data in A:
        # add latest + current
        _next = _current + data
        # if two sum is larger than max, max = next
        if _next > _max:
            _max = _next
        # if two sum is larger than 0, current = next
        if _next > 0:
            _current = _next
        else:
            _current = 0
        # if data is larger than current, current and max set to data
        if data > _max:
            _max = data
            _current = data
    # return max value
    return _max
