with open('./text3.txt', 'r') as f:
    lines = f.readlines()

print(lines)

total_ratio = 1
for num in range(len(lines)-1):
    gear1 = False
    gear2 = False
    multi_gears_1 = ""
    multi_gears_2 = ""
    #ratio = 1
    if "|" in lines[num]:
        multi_gears_1 = lines[num].split("|")
        print(multi_gears_1)
        gear1 = True
    if "|" in lines[num+1]:
        multi_gears_2 = lines[num+1].split("|")
        print(multi_gears_2)
        gear2 = True
    if(gear1):
        if(gear2):
            ratio = float(multi_gears_1[1])/float(multi_gears_2[0])
        else:
            ratio = float(multi_gears_1[1])/float(lines[num+1])
    elif(gear2):
        ratio = float(lines[num])/float(multi_gears_2[0])
    else:
        ratio = float(lines[num])/float(lines[num+1])
    print(ratio)
    total_ratio = total_ratio * ratio
print(f"Final total ratio:{total_ratio}")
#print(10000000000000/total_ratio)