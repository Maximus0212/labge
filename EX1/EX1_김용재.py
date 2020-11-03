import sys

f = sys.argv[1]

with open(f, 'r') as handle:
    domain_d = {}
    value_d = {}
    line_l = []
    
    for line in handle:
	line = line.strip().split()
	line_l.append(line)

    #print(line_l)

# domain
    for i in range(len(line_l)):
	if line_l[i][0] in domain_d:
	    if line_l[i][1] not in domain_d[line_l[i][0]]:
		domain_d[line_l[i][0]].append(line_l[i][1])
	else:
	    l_values = []
	    l_values.append(line_l[i][1])
	    domain_d[line_l[i][0]] = l_values

    #print(domain_d)
	
    tmp = []
    domain_l = []
    for k,v in domain_d.items():
        temp = [k,v]
        domain_l.append(temp)
    #print(domain_l)
	
    for s in range(len(line_l)):
        if line_l[s][0] in value_d:
            value_d[line_l[s][0]] += int(line_l[s][2])
        else:
            v_values = int(line_l[s][2])
            value_d[line_l[s][0]] = v_values
	    
        value_l = []
        IPI_l = []
    for k,v in value_d.items():
        value_l.append(v)
        IPI_l.append(k)

#    print(value_l)
#    print(IPI_l)
	
    total_l = []
    for x in range(len(domain_l)):
	domain_l[x].append(value_l[x])
	total_l.append(domain_l)

#domain 4 
    domain_4 = []
    for i in range(len(total_l)):
	if len(total_l[0][i][1]) == 4:
	    domain_4.append(total_l[0][i])
    sort_domain_4 = sorted(domain_4)
	

#output
    with open('result.txt','w') as file:
	for i in range(len(sort_domain_4)):
	    file.write(sort_domain_4[i][0]+'\t'+",".join(sort_domain_4[i][1])+'\t'+str(sort_domain_4[i][2])+'\n')








