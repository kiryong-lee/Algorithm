
import re

def solution(s):
    s = s.lower()
    s = re.sub(r' +.', lambda match: match.group(0).upper(), s)
    s = s[0].upper() + s[1:]
    return s
