# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/I
t = int(input(''))

for _ in range(t):
    min = 0
    n = int(input(''))
    x = list(map(int, input().split()))
    x = x[0 : n]
    min = x[0] + x[1] + 1
    for i in range (len(x)-1):
        for j in range (i+1 , len(x)):
            num = x[i] + x[j] + j-i
            if num < min: 
                min = num
    print(min)

