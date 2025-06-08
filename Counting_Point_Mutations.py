DNA_A = input()
DNA_B = input()

sequence_len = len(DNA_A)

HAMMING = 0

for i in range(sequence_len):
    if DNA_A[i] != DNA_B[i]:
        HAMMING += 1

print(HAMMING)