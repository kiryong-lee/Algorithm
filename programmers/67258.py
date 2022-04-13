
def solution(gems):
    n = len(set(gems))
    gem_dict = dict()
    start_pos = -100000
    end_pos = 0
    min_gem = ''
    for i, gem in enumerate(gems, start = 1):
        gem_dict[gem] = i
        
        if len(gem_dict) == n:
            if min_gem == '' or gem == min_gem:
                min_gem = gems[min(gem_dict.values()) - 1]
            _min = gem_dict[min_gem]

            if i - _min < end_pos - start_pos:
                end_pos = i
                start_pos = _min

    return [start_pos, end_pos]
