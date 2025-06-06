months, litter_size = map(int, input().split())

FibArray = [1, 1]

for i in range(2, months+1):
    FibArray.append(FibArray[i - 1] + FibArray[i - 2]*litter_size)

print(FibArray[months-1])




