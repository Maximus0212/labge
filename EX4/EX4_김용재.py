import sys
f = sys.argv[1]

with open(f, 'r') as data:
	TC_dic = {}
	for line in data:
		lines = line.strip().split('\t')
		GO = lines[0]
		TC_list = lines[1].split(',')
		for TC in TC_list:
			if TC == "":
				continue
			elif TC in TC_dic:
				TC_dic[TC].append(GO)
			else:
				GO_values = []
				GO_values.append(GO)
				TC_dic[TC] = GO_values

TC_GO = []

for k,v in TC_dic.items():
	tmp = [k,v]
	TC_GO.append(tmp)

with open('result_1.txt','w') as file:
	for i in range(len(TC_GO)):
		file.write(TC_GO[i][0]+'\t'+",".join(TC_GO[i][1])+'\t'+str(len(TC_GO[i][1]))+'\n')	
