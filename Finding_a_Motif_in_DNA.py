import re

dna = input()
dna_substring = input()

# regex matching which will include finding overlapping cases
positions = [match.start() for match in re.finditer('(?='+dna_substring+')', dna)]

ans = []

for p in positions:
    var = int(p) + 1
    print(var, end=" ")
