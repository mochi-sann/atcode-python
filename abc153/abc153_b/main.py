# Code for B - Common Raccoon vs Monster
# Use input() to fetch data from STDIN
h, n = map(int, input().split())
a = list(map(int, input().split()))

# print(sum(a))

if sum(a) >= h :
    print("Yes")
else:
    print("No")
