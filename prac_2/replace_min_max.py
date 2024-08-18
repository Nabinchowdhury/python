# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/M
n = int(input())
a = list(map(int, input().split()))[0:n]
min = a[0]
max = a[0]
for i in range(n):
    if a[i] < min:
        min = a[i]
    if a[i] > max:
        max = a[i]
temp_max_index = a.index(max)
a[a.index(min)] = max 
a[temp_max_index] = min
print(' '.join(map(str, a)))