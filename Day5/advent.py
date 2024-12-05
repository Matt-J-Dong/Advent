with open('./text.txt', 'r') as f:
    lines = f.readlines()
n = len(lines)

total = 0
rules = []
flag = False
for line in range(n):
    lines[line] = lines[line].strip()
    #print(lines[line])
    if(lines[line].find("|")>-1):
        #print("lol")
        rules.append(lines[line].split("|"))
    if(flag==True):
        good_line = True
        for rule in rules:
            location1 = lines[line].find(rule[0])
            location2 = lines[line].find(rule[1])
            if(location1>location2 and location1 != -1 and location2 != -1):
                good_line = False
                #print(f"Rule:{rule}")
                #print(f"Location 1: {lines[line][location1]}")
                #print(f"Location 2: {lines[line][location2]}")
            else:
                pass
        if(good_line==True):
            print("GOOD LINE")
            num = lines[line].split(",")
            print(num)
            num2 = num[len(num)//2]
            print(num2)
            total = total+int(num2)
        else:
            print("BAD LINE")
    if(lines[line]==""):
        flag = True
    
print(total)
            