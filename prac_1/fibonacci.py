# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/O

# def fib(n):
#     a, b = 0, 1
#     for _ in range(n - 2): 
#         temp = a
#         a = b
#         b = temp + b
#     return b
# def fib(n):
#     a, b = 0, 1
#     for _ in range(3, n+1): 
#         temp = a
#         a = b
#         b = temp + b
#     return b

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


# Input
N = int(input().strip())

# Output
print(fib(N))
