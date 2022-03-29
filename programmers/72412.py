
import itertools
import bisect

def solution(info, query):
    combinations = [()]
    combinations += list(itertools.combinations(range(4), 1))
    combinations += list(itertools.combinations(range(4), 2))
    combinations += list(itertools.combinations(range(4), 3))
    combinations += list(itertools.combinations(range(4), 4))
    
    info_dictionary = dict()
    for i in info:
        v = i.split(' ')
        v[4] = int(v[4])
        for combination in combinations:
            copy = list(v[:4])
            for index in combination:
                copy[index] = '-'
        
            key = ''.join(copy)
            if key in info_dictionary:
                info_dictionary[key].append(v[4])
            else:
                info_dictionary[key] = [v[4]]
    
    for k, v in info_dictionary.items():
        v.sort()
    
    answer = []
    for q in query:
        key = q.split(' ')
        limit = int(key[7])
        key = key[0] + key[2] + key[4] + key[6]

        if key in info_dictionary:
            answer.append(len(info_dictionary[key]) - bisect.bisect_left(info_dictionary[key], limit))
        else:
            answer.append(0)
            
    return answer
