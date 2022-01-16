
max_num = 0
max_pos = 0
for i in range(9):
    num = int(input())
    if num > max_num:
        max_num = num
        max_pos = i

print(max_num)
print(max_pos + 1)
