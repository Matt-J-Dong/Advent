with open('./text.txt', 'r') as f:
    lines = f.readlines()
n = len(lines)

total = 0
zeros = []
graph = []
for output in range(n):
    lines[output] = lines[output].strip()
    line = lines[output]
    print(line)
    for index, char in enumerate(line):
        if(char=="0"):
            zeros.append((index,output))
        graph.append(line)
print(zeros)
for zero in zeros:
    if()