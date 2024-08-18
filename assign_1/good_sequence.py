# https://atcoder.jp/contests/arc087/tasks/arc087_a
n = int(input())
s = list(map(int, input().split()))[0:n]
to_del = 0
data = {}
for item in s:
    if item in data:
        data[item] += 1
    else:
        data[item] = 1

for key, value in data.items():
    if int(key) != value:
        if(value < int(key)):
            to_del += value
        else:
            to_del += value - int(key)
print(to_del)