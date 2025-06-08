from Bio import SeqIO

# store all the results here, which can be sorted to find the highest
results = {}

file = open('input.fasta')



for seq_record in SeqIO.parse(file, "fasta"):
    
    cg_count = 0
    total_count = len(seq_record.seq)
    #print("total count", total_count)

    for rec in seq_record.seq:
        #print(rec)
        if rec == "C":
            cg_count += 1
            
        if rec == "G":
            cg_count += 1

        #print("gccount", cg_count)
    
    gc_content_percent = (cg_count/total_count)*100
    #print(cg_count, total_count)
    results[seq_record.id] = gc_content_percent
    #print("GC content is: ", gc_content_percent)


descending_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
for i in descending_results:
    print(i[0], "\n", i[1])