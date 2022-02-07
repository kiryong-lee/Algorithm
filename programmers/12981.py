
def solution(n, words):
    loop, index = 1, 1
    last_character = words[0][0]
    history_dict = dict()
    out = False
    for word in words:
        if word not in history_dict:
            if last_character != word[0]:
                out = True
                break            
            history_dict[word] = word
            last_character = word[-1]
        else:
            out = True
            break
        
        index += 1
        if index == n + 1:
            index = 1
            loop += 1

    if out:
        return [index, loop]
    else:
        return [0, 0]
