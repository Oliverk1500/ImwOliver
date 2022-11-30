import sys

num=(sys.argv[1:])

x = 0

for i in num:
    x += float(i)
    

print(x // len(num))