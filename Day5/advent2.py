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
            pass
            #print("GOOD LINE DON'T ADD")
        else:
            nums = lines[line].split(",")
            #print("BAD LINE ADD")
            print(nums)
            for rule in rules:
                find = 0
                flag2 = True
                try:
                    while(flag2==True):
                        #print("LOOP")
                        if(find==0):
                            location1 = nums.index(rule[0])
                            location2 = nums.index(rule[1])
                        if(find>0):
                            location1 = nums.index(rule[0],location1+1)
                            location2 = nums.index(rule[1],location2+1)
                            print(f"Location 1: {location1}")
                            print(f"Location 2: {location2}")
                        if(location1>location2):
                            print(f"Rule:{rule}")
                            #print(f"Location 1: {location1}")
                            #print(f"Location 2: {location2}")
                            remove = nums.pop(location2)
                            nums.insert(location1,remove)
                            print(f"New list:{nums}")
                            find = find+1
                        else:
                            flag2=False
                except:
                    pass
            for rule in rules:
                find = 0
                flag2 = True
                try:
                    while(flag2==True):
                        #print("LOOP")
                        if(find==0):
                            location1 = nums.index(rule[0])
                            location2 = nums.index(rule[1])
                        if(find>0):
                            location1 = nums.index(rule[0],location1+1)
                            location2 = nums.index(rule[1],location2+1)
                            print(f"Location 1: {location1}")
                            print(f"Location 2: {location2}")
                        if(location1>location2):
                            print(f"Rule:{rule}")
                            #print(f"Location 1: {location1}")
                            #print(f"Location 2: {location2}")
                            remove = nums.pop(location2)
                            nums.insert(location1,remove)
                            print(f"New list:{nums}")
                            find = find+1
                        else:
                            flag2=False
                except:
                    pass
            for rule in rules:
                find = 0
                flag2 = True
                try:
                    while(flag2==True):
                        #print("LOOP")
                        if(find==0):
                            location1 = nums.index(rule[0])
                            location2 = nums.index(rule[1])
                        if(find>0):
                            location1 = nums.index(rule[0],location1+1)
                            location2 = nums.index(rule[1],location2+1)
                            print(f"Location 1: {location1}")
                            print(f"Location 2: {location2}")
                        if(location1>location2):
                            print(f"Rule:{rule}")
                            #print(f"Location 1: {location1}")
                            #print(f"Location 2: {location2}")
                            remove = nums.pop(location2)
                            nums.insert(location1,remove)
                            print(f"New list:{nums}")
                            find = find+1
                        else:
                            flag2=False
                except:
                    pass
            for rule in rules:
                find = 0
                flag2 = True
                try:
                    while(flag2==True):
                        #print("LOOP")
                        if(find==0):
                            location1 = nums.index(rule[0])
                            location2 = nums.index(rule[1])
                        if(find>0):
                            location1 = nums.index(rule[0],location1+1)
                            location2 = nums.index(rule[1],location2+1)
                            print(f"Location 1: {location1}")
                            print(f"Location 2: {location2}")
                        if(location1>location2):
                            print(f"Rule:{rule}")
                            #print(f"Location 1: {location1}")
                            #print(f"Location 2: {location2}")
                            remove = nums.pop(location2)
                            nums.insert(location1,remove)
                            print(f"New list:{nums}")
                            find = find+1
                        else:
                            flag2=False
                except:
                    pass
            for rule in rules:
                find = 0
                flag2 = True
                try:
                    while(flag2==True):
                        #print("LOOP")
                        if(find==0):
                            location1 = nums.index(rule[0])
                            location2 = nums.index(rule[1])
                        if(find>0):
                            location1 = nums.index(rule[0],location1+1)
                            location2 = nums.index(rule[1],location2+1)
                            print(f"Location 1: {location1}")
                            print(f"Location 2: {location2}")
                        if(location1>location2):
                            print(f"Rule:{rule}")
                            #print(f"Location 1: {location1}")
                            #print(f"Location 2: {location2}")
                            remove = nums.pop(location2)
                            nums.insert(location1,remove)
                            print(f"New list:{nums}")
                            find = find+1
                        else:
                            flag2=False
                except:
                    pass
            for rule in rules:
                find = 0
                flag2 = True
                try:
                    while(flag2==True):
                        #print("LOOP")
                        if(find==0):
                            location1 = nums.index(rule[0])
                            location2 = nums.index(rule[1])
                        if(find>0):
                            location1 = nums.index(rule[0],location1+1)
                            location2 = nums.index(rule[1],location2+1)
                            print(f"Location 1: {location1}")
                            print(f"Location 2: {location2}")
                        if(location1>location2):
                            print(f"Rule:{rule}")
                            #print(f"Location 1: {location1}")
                            #print(f"Location 2: {location2}")
                            remove = nums.pop(location2)
                            nums.insert(location1,remove)
                            print(f"New list:{nums}")
                            find = find+1
                        else:
                            flag2=False
                except:
                    pass
            num2 = nums[len(nums)//2]
            print(num2)
            total = total+int(num2)
            #3468 not right
    if(lines[line]==""):
        flag = True
    
print(total)