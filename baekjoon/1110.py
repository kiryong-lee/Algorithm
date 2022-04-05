
target = int(input())
next = 0
count = 1
if target < 10:
    next = target * 10 + target
else:
    a, b = target // 10, target % 10
    next = b * 10 + (a + b) % 10

while target != next:
    a, b = next // 10, next % 10
    next = b * 10 + (a + b) % 10
    count += 1
   
print(count)
