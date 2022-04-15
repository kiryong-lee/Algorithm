
n = int(input())
for i in range(n):
    ox_list = input()
    ox_sum = 0
    score = 0
    for ox in ox_list:
        if ox == 'O':
            score += 1
        else:
            score = 0
        ox_sum += score
    print(ox_sum)
