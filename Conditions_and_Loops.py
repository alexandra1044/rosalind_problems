a, b = map(int, input().split())

total = 0

for i in range(a, b, 1):
    if i % 2 == 1:
        total = total + i


print(total)