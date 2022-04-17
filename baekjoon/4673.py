
not_self_dict = dict()
for i in range(1, 10001):
    if str(i) not in not_self_dict:
        print(i)
    dn = i
    while i > 0:
        dn += i % 10
        i //= 10
    not_self_dict[str(dn)] = True
