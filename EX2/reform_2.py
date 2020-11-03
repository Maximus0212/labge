
header = None
with open(f, 'r') as handle:
    for line in handle:
        line = line.strip()
        if line.startswith('>'):
            if header:
                fasta_dic[header] = seq
            header = line[1:]
            fasta_dic[header] = ''
            seq = ''
        else:
            seq += line
    if header:
        fasta_dic[header] = seq
        
        
    