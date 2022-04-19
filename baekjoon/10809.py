
string = input()
result = ['-1'] * 26
for i, s in enumerate(string):
    if result[ord(s) - 97] == '-1':
        result[ord(s) - 97] = str(i)
print(' '.join(result))
