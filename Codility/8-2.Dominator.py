# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# https://app.codility.com/demo/results/trainingQN3BTB-574/
def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return -1
    
    my_map = dict()
    max_count = 0
    max_value = -1
    # make map
    for data in A:
        if data in my_map:
            my_map[data] = my_map[data] + 1
        else:
            my_map[data] = 1
        # get candidate dominator
        if my_map[data] > max_count:
            max_count = my_map[data]
            max_value = data
    # return index of any element of array A in which the dominator of A occurs
    if max_count > len(A) // 2:
        for i, data in enumerate(A):
            if data == max_value:
                return i
    # else, return -1
    else:
        return -1
