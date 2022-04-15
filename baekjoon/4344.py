
n = int(input())
for i in range(n):
    score = list(map(int, input().split(' ')))
    score = score[1:]
    average = sum(score) / len(score)
    over_average = sum(i > average for i in score)
    print("%.3f" % (over_average * 100 / len(score)) + "%")
