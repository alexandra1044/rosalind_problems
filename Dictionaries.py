with open('input.txt') as f:
    data = f.read().split()

#data = input().split()

d = dict()

for line in data:
    line = line.strip()

    words = line.split(" ")
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

for key in list(d.keys()):
    print(key, "", d[key])
