a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
l = []
n = int(input());
for i in a:
    if i < n:
        l.append(i)
print(l)