text = ''.join(map(str, input()))

a, b, c, d = map(int, input().split())

x = slice(a, b + 1)

y = slice(c, d + 1)

# need the + 1 in order to slice inclusively, as python by default slices exclusively
print(text[x], text[y])