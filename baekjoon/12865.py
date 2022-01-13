
N, K = map(int, input().split())
max_value = [[0] * (K + 1) for i in range(N)]
for i in range(N):
    weight, value = map(int, input().split())
    for j in range(K + 1):
        if j < weight:
            # max_value[-1][j] : no problem because of 0
            max_value[i][j] = max_value[i - 1][j]
        else:
            max_value[i][j] = max(max_value[i - 1][j], value + max_value[i - 1][j - weight])

print(max_value[N - 1][K])
