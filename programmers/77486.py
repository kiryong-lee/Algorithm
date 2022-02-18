
import math

def solution(enroll, referral, seller, amount):
    parent_dict = dict()
    money_dict = dict()
    for e, r in zip(enroll, referral):
        parent_dict[e] = r
        money_dict[e] = 0
    
    for s, a in zip(seller, amount):
        a = a * 100
        while s != '-' and a > 0:
            money_dict[s] += math.ceil(a * 0.9)
            a = math.floor(a * 0.1)
            s = parent_dict[s]
    
    return [money_dict[e] for e in enroll]
