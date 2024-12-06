with open('./text.txt', 'r') as f:
    lines = f.readlines()
n = len(lines)

total = 1
flag = False
blocks = []
for output in range(n):
    lines[output] = lines[output].strip()
    line = lines[output]
    print(line)
    if(line.find("^")>=0):
        current = [output,line.find("^")]
    location = 0
    flag2 = True
    flag3 = True
    while flag2 == True:
        if(flag3 == True): #HOWWWW
            loc = line.find("#")
        else:
            loc = line.find("#",location+1)
        if(loc>-1):
            #print(f"{loc}")
            blocks.insert(len(blocks),[output,loc])
            location = loc
            flag3 = False
        else:
            flag2 = False
guard = True
guard_direction = [[-1,0],[0,1],[1,0],[0,-1]]
num = 0
guard_location = current.copy()
print(blocks)
visits = [guard_location.copy()]
while guard == True:
    #print(guard_direction)
    #print(guard_location)
    guard_location[0] = guard_location[0]+guard_direction[num][0]
    guard_location[1] = guard_location[1]+guard_direction[num][1]
    if(guard_location in blocks):
        guard_location[0] = guard_location[0]-guard_direction[num][0]
        guard_location[1] = guard_location[1]-guard_direction[num][1]
        num=(num+1)%4
        #print(num)
    #print(guard_location)
    if(guard_location not in visits):
        #print("yoy")
        total = total+1
    visits.append(guard_location.copy())
    if(guard_location[0]>(n-1) or guard_location[0]<0 or guard_location[1]>(len(line)-1) or guard_location[1]<0):
        guard = False
        total = total - 1
    
#5241 not it
print(total)
        