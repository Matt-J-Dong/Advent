with open('./text.txt', 'r') as f:
    lines = f.readlines()
n = len(lines)
list1 =[]
list2 = []
for i in range(n):
    lines[i] = lines[i].strip()
    split = lines[i].split('   ')
    split[0] = int(split[0])
    split[1] = int(split[1])
    list1.append(split[0])
    list2.append(split[1])

list1.sort()
list2.sort()
total = 0


for i in range(n):
    num = int(list1[i])
    count = list2.count(num)
    total += count*num

print(total)