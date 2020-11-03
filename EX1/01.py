import sys
f = sys.argv[1]

with open(f, 'r') as handle:
    lines = []
    for line in handle:
        line = line.strip().split()
        lines.append(line)
    print(lines)
