
import re

def solution(s):
    if re.search('[a-zA-Z]', s) == None:  
        if len(s) == 4 or len(s) == 6:
            return True
        else:
            return False
    else:
        return False
