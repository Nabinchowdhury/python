# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/M
n = input('')
x = list(map(int, input().split()))
a = x[0:int(n)]
min = a[0]
max = a[0]
for i in a:
    if i < min: min = i
    if i > max: max = i
min_index = a.index(min) 
max_index = a.index(max)
a[min_index] = max
a[max_index] = min
op = ''
for i in a:
    if len(op) == 0 : op+= str(i)
    else: op = op +' '+ str(i)
print(op)
