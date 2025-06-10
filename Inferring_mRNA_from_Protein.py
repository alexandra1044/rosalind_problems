protein = (map(str, input()))

STOP = 3

codon_table = {
    'F':2,
    'L':6,
    'S':6,
    'Y':2,
    'C':2,
    'W':1,
    'P':4,
    'H':2,
    'Q':2,
    'R':6,
    'I':3,
    'M':1,
    'T':4,
    'N':2,
    'K':2,
    'V':4,
    'A':4,
    'D':2,
    'E':2,
    'G':4
}

total = 1

for p in protein:
    total = ((total * codon_table[p])) % 1000000

total = total * STOP

print(total)