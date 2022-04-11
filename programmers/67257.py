
import re
import itertools

def solution(expression):
    operators = ['+', '-', '*']
    _max = 0
    for operator in list(itertools.permutations(operators, 3)):
        exp = re.split(r'(\D)', expression)
        for oper in operator:
            while oper in exp:
                idx = exp.index(oper)
                if oper == '+':
                    exp[idx - 1] = str(int(exp[idx - 1]) + int(exp[idx + 1]))
                elif oper == '-':
                    exp[idx - 1] = str(int(exp[idx - 1]) - int(exp[idx + 1]))
                else:
                    exp[idx - 1] = str(int(exp[idx - 1]) * int(exp[idx + 1]))
                del exp[idx]
                del exp[idx]

        _max = max(_max, abs(int(exp[0])))
        
    return _max
