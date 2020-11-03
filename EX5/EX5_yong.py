import sys
f = sys.argv[1]

with open(f, 'r') as data:
	contents = data.read().splitlines()

lines = []
gene_name_list = []
correlation_value = []

for line in contents:
	token = line.split(' ')
	lines.append(token)
gene_name_l = lines[0]

for i in range(len(gene_name_l)):
	gene_name_list.append(gene_name_l[i].strip('"'))
#print(gene_name_list)
	correlation_value.append(lines[i+1][1:])
#print(correlation_value[0])

gene_dic = {}
gene_dic=dict(zip(gene_name_list, correlation_value))
#print(gene_dic)

gene_list_2 = []
for k,v in gene_dic.items():
	gene_list = []
	for s in range(len(gene_name_list)):
		if float(gene_dic[k][s]) >= 0.9:
			gene_list.append(gene_dic[k][s])
	#print(gene_list)	
	gene_list_2.append(gene_list)

#print(gene_list_2)

result_dic = {}
result_dic = dict(zip(gene_dic.keys(), gene_list_2))
#print(result_dic)
gene_list_4 = []
for k,v in result_dic.items():
	gene_list_3 = []
	for i in v:
		number = gene_dic[k].index(i)
		gene = gene_name_list[number]
		gene_list_3.append(gene)
	gene_list_4.append(gene_list_3)

	#print(number)

gene_len = []

for i in range(len(gene_name_list)):
	gene_len.append(len(gene_list_4[i]))

with open('result.txt', 'w') as file:
	for i in range(len(gene_list_4)):
		if result_dic.keys()[i] == " ".join(gene_list_4[i]):
			continue
		else:
			if result_dic.keys()[i] in gene_list_4[i]:
				gene_list_4[i].remove(result_dic.keys()[i])
		file.write(result_dic.keys()[i]+'\t'+str(gene_len[i]-1)+'\t'+" ".join(gene_list_4[i])+'\n')








