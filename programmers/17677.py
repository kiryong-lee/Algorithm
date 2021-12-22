
import re

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    set1 = [str1[i:i + 2] for i in range(len(str1) - 1) if re.match("[a-z][a-z]", str1[i:i + 2])]
    set2 = [str2[i:i + 2] for i in range(len(str2) - 1) if re.match("[a-z][a-z]", str2[i:i + 2])]
    intersect = []
    for x in set1:
        if x in set2:
            intersect.append(x)
            set2.remove(x)
    union = set1 + set2
    if union == []:
        return 65536
    else:
        return int(len(intersect) / len(union) * 65536)
