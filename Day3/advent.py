with open('./text.txt', 'r') as f:
    lines = f.readlines()
n = len(lines)

total = 0
for line in range(n):
    print(line)