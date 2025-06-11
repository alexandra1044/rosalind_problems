from itertools import permutations

genes = input()

g = []

permutation_count = 0

permutations_end = []

for i in range(1, int(genes)+1, 1):
    g.append(str(i))

#print(g)

# print statement here strips all the commas and brackets
for p in permutations(g, int(genes)):
    permutation_count += 1
    permutations_end.append(p)

print("\n")

print(permutation_count)


for p in permutations_end:
    print(" ".join(map(str,p)))
