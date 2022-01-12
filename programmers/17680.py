
def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    
    lru = []
    time = 0
    for city in cities:
        if city.lower() in lru:
            time += 1
            lru.pop(lru.index(city.lower()))
            lru.append(city.lower())
        else:
            time += 5
            if len(lru) == cacheSize:
                lru.pop(0)
            lru.append(city.lower())
    
    return time
