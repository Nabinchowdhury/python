# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/N
a, b = map(int,input().split())
x = input('')
s = x[0:int(a)+ int(b)+1]
# print(s)
if s[int(a)] != '-':
    print('No')
else:
    flag = True
    for i in range(int(len(s))):
        if i == int(a): continue
        if s[i].isnumeric() is False or int(s[i]) < 0 or int(s[i]) > 9:
            flag = False
            break
    if(flag): print('Yes')
    else: print('No')

# 1 1
# 12-
# 3 3
# 269-665
# a = '1-'
# print(a.isnumeric())