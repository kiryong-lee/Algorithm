
import math
import sys

n = int(input())
result = 1
min_num = 2000000000
max_num = 1
num_list = list(map(int, sys.stdin.readline().split()))
for num in num_list:
    if min_num > num:
        min_num = num
    if max_num < num:
        max_num = num
    
    result = result * num // math.gcd(result, num)
    
if result == max_num:
    print(result * min_num)
else:
    print(result)
