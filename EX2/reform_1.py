def reform(fileName: str) -> None:
    with open(fileName, 'r') as handle:
        tmp = ''
        for line in handle:
            if line.startswith('>'):
                ids.append(line.rstrip())
                if tmp != '':
                    seqs.append(tmp)
                    tmp = ''
                continue
            line = line.strip()
            tmp += line
        seqs.append(tmp)
    return ids, seqs
 
ids = list()
seqs = list()
ids, seqs = reform("FSMtest.txt")


            