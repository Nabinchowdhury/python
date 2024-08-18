# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/G
n = int(input())
a = input().split()[0:n]
str_a = ''.join(a)
str_rev_a = ''.join(a[::-1])
if str_a == str_rev_a:
    print("YES")
else:
    print("NO")
