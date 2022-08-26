from collections import defaultdict

def solution(survey, choices):
    
    type_dict = defaultdict(int)
    for s, c in zip(survey, choices):
        if c > 4:
            if s[1] in type_dict:
                type_dict[s[1]] += c - 4
            else:
                type_dict[s[1]] = c - 4
        elif c < 4:
            if s[0] in type_dict:
                type_dict[s[0]] += 4 - c
            else:
                type_dict[s[0]] = 4 - c
    
    answer = ''
    if type_dict['R'] < type_dict['T']:
        answer += 'T'
    else:
        answer += 'R'
    
    if type_dict['C'] < type_dict['F']:
        answer += 'F'
    else:
        answer += 'C'
    
    if type_dict['J'] < type_dict['M']:
        answer += 'M'
    else:
        answer += 'J'
    
    if type_dict['A'] < type_dict['N']:
        answer += 'N'
    else:
        answer += 'A'
    
    return answer
