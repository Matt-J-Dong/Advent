with open('./text3.txt', 'r') as f:
    lines = f.readlines()

names = lines[0].split(',')
instructions = lines[2].split(',')
ptr = 0

print(names)
print(instructions)
print(len(names)-1)
print(len(instructions)-1)

for i in instructions:
    #print(len(i))
    #print(f"Position:{ptr}")
    #print(f"Name:{names[ptr]}")
    print(names)
    ptr = 0
    if i[0]=="L":
        num = int(i[1:len(i)])
        while(num>0):
            ptr=ptr-1
            num=num-1
        ptr = ptr%(len(names))
        temp = names[ptr]
        names[ptr] = names[0]
        names[0] = temp
    else:
        num = int(i[1:len(i)])
        while(num>0):
            ptr=ptr+1
            num=num-1
        ptr = ptr%(len(names))
        temp = names[ptr]
        names[ptr] = names[0]
        names[0] = temp
    
#ptr = ptr%(len(names))
#print(ptr)
print(names[0]) #Elvarcoryx