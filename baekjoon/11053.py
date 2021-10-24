N = int(input())
A = list(map(int, input().split()))

B = [1] * N
max_val = 1
for i in range(1, N):
    b = 0
    for j in range(i):
        if A[j] < A[i] and b < B[j]:
            b = B[j]
    if b != 0:
        B[i] = b + 1
    if B[i] > max_val:
        max_val = B[i]

print(max_val)
