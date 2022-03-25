
def solution(msg):
    dictionary = dict()
    for i in range(26):
        dictionary[chr(65 + i)] = i + 1

    n = len(msg)
    answer = []
    last_num = 27
    i = 0
    while i < n:
        wc = msg[i]
        j = i + 1
        while j < n and wc in dictionary:
            wc += msg[j]
            j += 1
        if j == n:
            if wc in dictionary:
                answer.append(dictionary[wc])
                break

        w = wc[:-1]
        c = wc[-1]
        answer.append(dictionary[w])
        if wc not in dictionary:
            dictionary[wc] = last_num
            last_num += 1

        i = j - 1

    return answer
