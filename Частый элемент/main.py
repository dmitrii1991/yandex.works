n = int(input())
a = [int(i) for i in input().split(' ')]

number, count = 0, 0

for i in set(a):
    print(i)
    if a.count(i) > count:
        number = i
        count = a.count(i)

print(number)
