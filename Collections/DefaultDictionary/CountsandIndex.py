from collections import defaultdict

s = input()
t = tuple( s.split(" "))
n = int(t[0])
m = int(t[1])

l = []
for i in range(n):
    l.append(input())


dic = defaultdict(list)
for i, ch in enumerate(l):
    dic[ch].append(i+1)

for i in range(m):
    ch = input()
    if ch in dic is not None:
        w = " ".join(str(j) for j in dic[ch])
        print(w)
    else:
        print(-1)
