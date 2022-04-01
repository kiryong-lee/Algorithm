
def get_count(s, n, f, e):
    count = e - f - 1
    while f >= 0 and e < n:
        if s[f] == s[e]:
            f -= 1
            e += 1
            count += 2
        else:
            break
    
    return count


def solution(s):
    n = len(s)
    max_palindrome = 1
    for i in range(n - 1):
        f, e = i - 1, i + 1
        count = get_count(s, n, f, e)
        max_palindrome = max(max_palindrome, count)
        
        if s[i] == s[i + 1]:
            f = i - 1
            e = i + 2
            count = get_count(s, n, f, e)
            max_palindrome = max(max_palindrome, count)
        
    return max_palindrome
