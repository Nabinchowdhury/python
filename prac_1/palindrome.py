# https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/I
num_str = input('')
num = int(num_str)
rev = 0
count = 0
def revNumber (number, reverse):
    if int(number/10) != 0:
        remainder = number % 10
        if reverse == 0 and remainder == 0 :
            reverse = reverse
        else : reverse = reverse*10 + remainder
        return revNumber(int(number/10), reverse)
    else:
        reverse =reverse*10 + number
    return reverse
reversed_number = revNumber(num, rev)
if len(num_str) > 1:
    print(num_str[::-1].lstrip('0'))
else: print(num_str)

if reversed_number == num:
    print('YES')
else : print('NO')
# str_N = '0'
    
#     # Reverse the string and remove leading zeroes
# reversed_N = str_N[::-1].lstrip('0')
# print(reversed_N, len(str_N))
# print(reversed_N)
# if 10%10 != 0:
#     print(True)

# print(int(1/10))

#for string palindrome
# print(num == num[::-1], num[::-1])
# temp = ''
# for i in num[::-1]:
#     if i == '0':
#         continue
#     else: temp += i
# print(temp)