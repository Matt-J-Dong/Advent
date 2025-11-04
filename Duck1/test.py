with open('./text.txt', 'r') as f:
    lines = f.readlines()

list1 = lines[0].split(',')
list2 = lines[2].split(',')
ptr = 0

print(list1)
print(list2)

for i in list2:
    # print(ptr)
    # print(list1[ptr])
    if i[0]=="L":
        num = int(i[1])
        while(ptr>0 and num>0):
            ptr=ptr-1
            num=num-1
    else:
        num = int(i[1])
        while(ptr<len(list1)-1 and num>0):
            ptr=ptr+1
            num=num-1

print(list1[ptr])