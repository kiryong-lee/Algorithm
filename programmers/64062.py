
def solution(stones, k):
    _min = min(stones)
    _max = max(stones)
    while _min < _max:
        _middle = int((_min + _max) / 2)
        if _middle == _min: # 무한루프 방지
            _middle = _min + 1

        jump_count = 1
        for stone in stones:
            if stone < _middle:
                jump_count += 1
                if jump_count > k: # 점프 못하면 최대 감소
                    _max = _middle - 1
                    break
            else:
                jump_count = 1
            
        if jump_count <= k: # 점프 가능하면 최소 증가
            _min = _middle

    return _min # 점프할 수 있는 최소가 정답
