with open('./text.txt', 'r') as f:
    lines = f.readlines()
n = len(lines)

total = 0
for output in range(n):
    lines[output] = lines[output].strip()
    line = lines[output]
    print(line)
    for char in line:
        if(char == "B"):
            total = total+1
        if(char == "C"):
            total = total+3
print(total)
