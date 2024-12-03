with open('./text.txt', 'r') as f:
    lines = f.readlines()
n = len(lines)

total = 0
for i in range(n):
    lines[i] = lines[i].strip()
    print(lines[i])
    flag = True
    while flag:
        print(f"Current string: {lines[i]}")
        index = lines[i].find("mul(")
        if(index==-1):
            flag = False
            break
        print(index)
        print(lines[i][index:len(lines[i])])
        end = lines[i][index:len(lines[i])].find(")")+index
        print(end)
        check = lines[i][index+4:end]
        numbers = check.split(",")
        print(numbers)
        #print("NUMBERS FOUND")
        number_list = map(int,numbers)
        try:
            number_list = list(number_list)
            print(number_list)
            total = total + number_list[0]*number_list[1]
            lines[i]=lines[i][end+1:len(lines[i])]
        except:
            lines[i]=lines[i][index+4:len(lines[i])]
        #print("EXCEPTION")
        #break
        print(f"After removal: {lines[i]}")
        print(f"Current total: {total}")


