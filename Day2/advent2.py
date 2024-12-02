with open('./text.txt', 'r') as f:
    lines = f.readlines()
n = len(lines)

total = 0
for i in range(n):
    lines[i] = lines[i].strip()
    split = lines[i].split(' ')
    #print(split)
    ints = [int(item) for item in split]
    positive = 0
    new_list = ints.copy()
    flag = False
    for idx, number in enumerate(ints):
        new_list = ints.copy()
        new_list.pop(idx)
        #print(new_list)
        positive = 0
        for index, num in enumerate(new_list):
            if(index!=0):
                difference = new_list[index]-new_list[index-1]
                #print(difference)
                if(difference>0 and difference<4):
                    positive += 1
                else:
                    if(difference<0 and difference>-4):
                        positive -= 1
            print(positive)
            if(abs(positive)==len(new_list)-1 and flag==False):
                flag = True
                total = total+1

print(f"Total={total}")