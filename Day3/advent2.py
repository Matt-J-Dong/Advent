with open('./text.txt', 'r') as f:
    lines = f.readlines()
n = len(lines)

total = 0
for i in range(n):
    lines[i] = lines[i].strip()
    print(lines[i])
    flag = True
    do_flag = True
    while flag:
        print(f"Current string: {lines[i]}")
        index = lines[i].find("mul(")
        do_index = lines[i].find("do()")
        donot_index = lines[i].find("don't()")
        if(do_index==-1):
            do_index= 9999
        if(donot_index==-1):
            donot_index= 9999
        if(index<do_index and index<donot_index):
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
                if(do_flag):
                    total = total + number_list[0]*number_list[1]
                lines[i]=lines[i][end+1:len(lines[i])]
            except:
                lines[i]=lines[i][index+4:len(lines[i])]
            #print("EXCEPTION")
            #break
            print(f"After removal: {lines[i]}")
            print(f"Current total: {total}")
        if(do_index<index and do_index<donot_index):
            print("TRUE!")
            do_flag = True
            lines[i]=lines[i][do_index+4:len(lines[i])]
        if(donot_index<index and donot_index<do_index):
            print("FALSE!")
            do_flag = False
            lines[i]=lines[i][donot_index+7:len(lines[i])]
print(total)