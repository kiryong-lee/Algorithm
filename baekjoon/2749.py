
n = int(input()) % 1500000

fibo = [0, 1, 1]
for i in range(1, n - 1):
	fibo[0] = fibo[1]
	fibo[1] = fibo[2]
	fibo[2] = (fibo[0] + fibo[1]) % 1000000

if n < 2:
	print(n)
else:
	print(fibo[2])
