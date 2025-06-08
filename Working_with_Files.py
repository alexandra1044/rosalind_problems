i = 1

file = open('input.txt')

for data in file.readlines():
        if i % 2 == 0:
            print(data)
        i += 1
