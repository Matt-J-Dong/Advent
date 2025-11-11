with open('./text2.txt', 'r') as f:
    lines = f.readlines()

print(lines)

total_ratio = 1
for num in range(len(lines)-1):
    ratio = float(lines[num])/float(lines[num+1])
    print(ratio)
    total_ratio = total_ratio * ratio
print(total_ratio)
print(10000000000000/total_ratio)