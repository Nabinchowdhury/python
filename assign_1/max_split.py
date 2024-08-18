# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/S?fbclid=IwAR1qi6o8WBDOrdzcZ--U5YO_40SSQmmLbZ8jggB6CFIRqog1ukVL_Z2wK2s
def max_split_balanced_string(S):
    count_L = 0
    count_R = 0
    substrings = []
    start_index = 0

    for i, char in enumerate(S):
        if char == 'L':
            count_L += 1
        elif char == 'R':
            count_R += 1
        
        if count_L == count_R:
            substrings.append(S[start_index:i+1])
            start_index = i + 1
            count_L = 0
            count_R = 0

    # Print results
    print(len(substrings))
    for substring in substrings:
        print(substring)

S = input().strip()
max_split_balanced_string(S)
# LLRRLLLRRR
# OutputCopy
# 2
# LLRR
# LLLRRR