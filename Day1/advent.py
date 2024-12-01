with open('./text.txt', 'r') as f:
    lines = f.readlines()
n = len(lines)
list1 =[]
list2 = []
for i in range(n):
    lines[i] = lines[i].strip()
    split = lines[i].split('   ')
    list1.append(split[0])
    list2.append(split[1])

list1.sort()
list2.sort()
total = 0
for i in range(n):
    num = abs(int(list2[i])-int(list1[i]))
    total += num

print(total)