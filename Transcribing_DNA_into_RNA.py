dna = input()

output = ""

for i in dna:
    if i == 'T':
        output += 'U'
    else:
        output += i
        
print(output)