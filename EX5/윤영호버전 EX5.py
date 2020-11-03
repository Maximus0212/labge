## 문제의 조건 상관관계 0.9 이상이면 gene name 을써준다.
with open('corNerve.txt', 'r') as data: # 데이터 열기
    contents = data.read().splitlines() # 한줄씩 읽고 

gene_name=contents[0].replace('"', '').split(' ') # " 다 없에고 ' ' 단위로 쪼개서 list에 저장

gene_name_dic={} # dic으로 설정 'PARD3': 1, 'RTN4': 2, 'ASZ1': 3, 'SLITRK6': 4, ~~ 67까지

gene_ind_dic={} # dic으로 설정 '0': PARD3 ~ 67 까지

for ind,gene in enumerate(gene_name):
    gene_name_dic[gene]=ind
    gene_ind_dic[ind]=gene

gene_cor_09_list=[] # 0.9 이상 상관관계 저장

for i in contents[1:]:
    gene_cor=i.replace('"', '').split(' ')
    gene_cor_09=[]
    num=0
    
    for ind, x in enumerate(gene_cor[1:]):
        
        if float(x) >0.9:
            num+=1
            gene_cor_09.append(ind)
    gene_cor_09.insert(0, num) # 0.9 상관관계 갯수
    gene_cor_09.insert(0,gene_name_dic[gene_cor[0]]) # 해당 유전자?
    
    gene_cor_09_list.append(gene_cor_09) # 0.9이상을 모두 저장
    
# 변수 중간 정리
# 1) 요인 이름 저장 gene_name_dic # dic으로 설정 'PARD3': 1, 'RTN4': 2, 'ASZ1': 3, 'SLITRK6': 4, ~~ 67까지

# 2) 요인 index 저장 gene_ind_dic'0': PARD3 ~ 67 까지

# 3) 상관관계 저장  gene_cor_0.9_list
# ['0,1, 0], '[1, 1, 1], ~ ]
        # index, (0.9 넘는 갯수) , index 형태
    

with open('result_yoon_ver.txt', 'w') as file:
    for i in gene_cor_09_list:
        if i[1] >1:
            file.write(f'{gene_ind_dic[i[0]]}\t{i[1]-1}')
            for x in i[2:]:
                if x != i[0]:
                    file.write(f'\t{gene_ind_dic[x]}')
            file.write('\n')