import sys

f = sys.argv[1]

# only rs number 
with open(f, 'r') as MCP:
    rs_mcp_l = []
    for line in MCP:
	lines = line.strip().split('\t')
        rs_mcp = lines[0]
	rs_mcp_split = rs_mcp.split("_")
	rs_mcp_l.append(rs_mcp_split[0])

with open('a.txt', 'r') as A:
    rs_a_l = []
    symbol_l = []
    func_l = []
    for line in A:
	lines = line.split('\t')
	rs_a = lines[1]
        rs_a_l.append(rs_a)
        gene_symbol = lines[6]
	symbol_l.append(gene_symbol)
	func = lines[7]
        func_l.append(func)

d = {}
d=dict(zip(rs_a_l, symbol_l))

d_f = {}
d_f = dict(zip(rs_a_l, func_l))

# duplicate rs_num
rs_dup = []
for dup in range(len(rs_mcp_l)):
    if rs_mcp_l[dup] in rs_a_l:
        rs_dup.append(rs_mcp_l[dup])

result_RS = []
result_SB = []
result_FU = []

for sym in range(len(rs_dup)):
    if d[rs_dup[sym]] == "":
	continue
    else:
	result_RS.append(rs_dup[sym])
	result_SB.append(d[rs_dup[sym]])

for fc in range(len(rs_dup)):
    if d_f[rs_dup[fc]] == "":
	continue
    else:
        result_FU.append(d_f[rs_dup[fc]])

with open('result.txt', 'w') as file:
    for i in range(len(result_RS)):
	file.write(result_RS[i]+'\t'+result_SB[i]+'\t'+result_FU[i]+'\n')














 
