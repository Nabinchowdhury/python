# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/Y
n, q = list(map(int, input().split()))
x = list(map(int, input().split()))
x = x[0 : n]
additions = []
a = 0
for i in range(len(x)):
    a += x[i]
    additions.append(a)
sums = []
for _ in range(q):
    l, r = list(map(int, input().split()))
    if l == 1:
        sums.append(additions[r-1])
    else :
        sums.append(additions[r-1] - additions[l-2])
# print(' '.join(str(s) for s in sums))
for s in sums:
    print(s)


# prefix_sum = [0] * (1 + 1)
# print(prefix_sum)
# 6 3
# 6 4 2 7 2 7
# 1 3
# 3 6
# 1 6