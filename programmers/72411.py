
import itertools

def solution(orders, course):
    n = len(orders)
    answer = []
    for c in course:
        dictionary = dict()
        for order in orders:
            for menu in itertools.combinations(order, c):
                str_value = ''.join(sorted(list(menu)))
                if str_value in dictionary:
                    dictionary[str_value] = dictionary[str_value] + 1
                else:
                    dictionary[str_value] = 1

        small_answer = []
        small_max = 2
        for menu in list(dictionary):
            if dictionary[menu] > small_max:
                small_max = dictionary[menu]
                small_answer = [menu]
            elif dictionary[menu] == small_max:
                small_answer.append(menu)

        answer += small_answer

    return sorted(answer)
