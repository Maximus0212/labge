import sys
d = sys.argv[1]
f = sys.argv[2]

with open(d, 'r') as data:
	contents = data.read().splitlines()

line_dic = {}
line_ind_dic = {}   

for ind, line in enumerate(contents):
	line = line.strip()
	line_dic[line] = ind
	line_ind_dic[ind] = line
#print(len(line_dic))          # ' ' : index --> not in order 
#print(len(line_ind_dic))       # index : ' ' -->  in order

CDS_line = []
locus_tag_list = []
for i in line_ind_dic:
	if line_ind_dic[i].startswith("CDS"):
		CDS_line.append(line_ind_dic[i].replace(" ",''))
		if line_ind_dic[i+1].startswith("/gene"):
			locus_tag_list.append(line_ind_dic[i+2][11:].replace('"',''))
		else:
			locus_tag_list.append(line_ind_dic[i+1][11:].replace('"',''))

#CDS_digit_list
CDS_digit_list = []
for i in CDS_line:
	digit = ""
	for s in i:
		if s.isdigit() or s == '.':
			digit += s	
	CDS_digit_list.append(digit.split('..'))
#print(CDS_digit_list)

fasta_seq = ''

with open(f, 'r') as fasta:
	for line in fasta:
		if line.startswith('>'):
			continue
		fasta_seq += line.strip()
#print(fasta_list[0])

fasta_list = []
for i in CDS_digit_list:
	fasta_list.append(fasta_seq[int(i[0]):int(i[1])+1])

#print(fasta_list)

fasta_dic = {}
fasta_dic = dict(zip(locus_tag_list, fasta_list))

with open('result_10.fasta','w') as file:
	for i in locus_tag_list[0:10]:
		file.write(">" + i + '\t' + str(len(fasta_dic[i])) + '\n')
		for s in range(0,len(fasta_dic[i]), 70):
			file.write(fasta_dic[i][s:s+70]+'\n')

comp_dic = {}
comp_ind = []
for ind, comp in enumerate(CDS_line):
	comp_dic[ind] = comp
	if 'complement' in comp_dic[ind]:
		comp_ind.append(ind)
	else:
		none_ind = ind 

with open('result_list.txt','w') as file:
	for i in comp_dic:
		file.write(str(i+1) + '\t' + locus_tag_list[i] +'\t')
		if i in comp_ind:
			file.write('complement'+'\t')
		else:
			file.write('none'+'\t')
		file.write(CDS_digit_list[i][0]+'\t'+CDS_digit_list[i][1]+'\n')


