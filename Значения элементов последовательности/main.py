n = int(input())
a = [int(i) for i in input().split()]

def Func(i):
    if i == 0 or i == 1 or i == 2:
        return i
    else:
        return Func(i-1) + Func(i-3)

for i in a:
    print(Func(i), end=' ')
