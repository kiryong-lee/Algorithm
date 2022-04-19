
_min = 51

def check(A, B):
    count = 0
    for a, b in zip(A, B):
        if a != b:
            count += 1
    
    if count > 1:
        return False
    else:
        return True


def traverse(target, words, use_list, order):
    global _min
    
    if order[-1] == target:
        if _min > len(order) - 1:
            _min = len(order) - 1
    
    for i, word in enumerate(words):
        if use_list[i] == False and check(word, order[-1]):
            use_list[i] = True
            order.append(word)
            traverse(target, words, use_list, order)
            use_list[i] = False
            order.pop()


def solution(begin, target, words):
    global _min
    
    use_list = [False] * len(words)
    order = [begin]
    traverse(target, words, use_list, order)
    
    if _min == 51:
        return 0
    else:
        return _min
