# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/P
def calcOp (arr):
    count = 0
    not_even = False
    for i, val in enumerate(arr):
        if val % 2 != 0:
           not_even = True
           break
        else : arr[i] =(val/2)
    if not_even: 
        return count
    else:
        count += 1 + calcOp (arr)
        return count
 
n = int(input())
s = list(map(int, input().split()))[0:n]
print(calcOp(s))