from Bio import SeqIO

file = open('input.fasta')

dna = []

def find_lcs(strings):
    longest_substring = ''
    if len(strings) < 2 or len(strings[0]) == 0:
        return longest_substring
    
    for start in range(len(strings[0])):
        for length in range(1, len(strings[0]) - start + 1):
            current_substring = strings[0][start:start + length]
            if len(current_substring) > len(longest_substring) and all(current_substring in other for other in strings):
                longest_substring = current_substring
                
    return longest_substring

   
for seq_record in SeqIO.parse(file, "fasta"):
    #print(seq_record.seq)
    dna.append(str(seq_record.seq))
    
ans = find_lcs(dna)

print(ans)