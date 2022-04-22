
from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def minimality(col, key_list):
    for key in key_list:
        if set(key).issubset(set(col)):
            return False
    return True


def uniqueness(col, relation):
    check_dict = dict()
    for i in range(len(relation)):
        value = ''
        for c in col:
            value += relation[i][c] + "^"
        if value in check_dict:
            return False
        check_dict[value] = value
        
    return True


def solution(relation):
    result = 0
    sets = list(powerset(range(len(relation[0]))))
    key_list = []
    for col in sets:
        if not col or not minimality(col, key_list):
            continue
        
        if uniqueness(col, relation):
            result += 1
            key_list.append(col)
        
    return result
