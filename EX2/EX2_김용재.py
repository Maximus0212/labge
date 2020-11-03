import sys

f = sys.argv[1]

fasta_dict = {}
seq = ''
header = None 
with open(f, 'r') as handle:
    for line in handle:
	line = line.strip()
	if line.startswith(">"):
	    if header:
		fasta_dict[header] = seq
	    header = line[1:]
	    fasta_dict[header] = ''
	    seq = ''
	else:
	    seq += line
    if header:
	fasta_dict[header] = seq

    #print(fasta_dict)

    header_l = []
    seq_l = []
    for k,v in fasta_dict.items():
	header_l.append(k)
	seq_l.append(v)
    #print(header_l)

# list single_linkagne header 
single = open('single_linkagne.txt', 'r')
read_file = single.readline()
single_h = read_file.strip().split(" ")
#print(single_h)

fasta_d_k = []
fasta_d_v = []
for k,v in fasta_dict.items():
    fasta_d_k.append(k)
    fasta_d_v.append(v)

#print(len(single_h)) #644

with open('output.fasta', 'w') as file:
    for i in range(len(single_h)):
        if single_h[i] in fasta_d_k:
	    file.write(">"+single_h[i]+'\n'+fasta_dict[single_h[i]]+'\n')
	


















