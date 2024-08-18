# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/Q
# def reverse(str):
#     return str[::-1]
# or
# reverse = lambda str: str[::-1]

s_list = input('').split()
rev_s_list = list(map(lambda str: str[::-1], s_list))
print(' '.join(rev_s_list)) 