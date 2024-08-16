# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/M
a, b = input('').split()
op = ''
for i in range(int(a), int(b)+1):
    str_i = str(i)
    # print(str_i)
    is_lucky = False
    for j in str_i:
        if int(j) == 4 or int(j) == 7:
           is_lucky = True
        else : 
            is_lucky = False
            break
    if(is_lucky is True):
        if(len(op) == 0): op+=str_i
        else: op = op +' ' + str_i
if(op != ''): print(op)
else: print(-1)
# a = '7'
# print(int(a) == 4 or int(a) ==7)
# op = ';'
# op = op + ' ' + "str_i"
# print(op)