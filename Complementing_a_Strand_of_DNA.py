dna = input()

output = ""

for i in dna:
    if i == 'A':
        output += 'T'
    elif i == 'T':
        output += 'A'
    elif i == 'C':
        output += 'G'
    elif i == 'G':
        output += 'C'
 
        
print(output[::-1])