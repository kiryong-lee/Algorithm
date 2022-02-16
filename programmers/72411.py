
import itertools

def solution(orders, course):
    n = len(orders)
    dictionary = dict()
    for c in course:
        for i in range(n):
            for j in range(i + 1, n):
                common = set(orders[i]).intersection(set(orders[j]))
                if len(common) >= c:
                    for menu in itertools.combinations(common, c):
                        str_value = ''.join(sorted(list(menu)))
                        if str_value in dictionary:
                            dictionary[str_value] = dictionary[str_value] + 1
                        else:
                            dictionary[str_value] = 1
    
    answer = []
    for c in course:
        small_answer = []
        small_max = 0
        for menu in list(dictionary):
            if len(menu) == c:
                if dictionary[menu] > small_max:
                    small_max = dictionary[menu]
                    small_answer = [menu]
                elif dictionary[menu] == small_max:
                    small_answer.append(menu)
        
        for menu in small_answer:
            answer.append(menu)
    
    return sorted(answer)
