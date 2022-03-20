
import math

def solution(n, stations, w):
    count = 0
    interval = 2 * w + 1
    distance = stations[0] - w - 1
    if distance > 0:
        count = math.ceil(distance / interval)

    for i in range(1, len(stations)):
        distance = stations[i] - stations[i - 1] - interval
        if distance > 0:
            count += math.ceil(distance / interval)

    distance = n - stations[-1] -  w
    if distance > 0:
        count += math.ceil(distance / interval)

    return count
