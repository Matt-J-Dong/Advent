with open('./text.txt', 'r') as f:
    lines = f.readlines()
n = len(lines)

total = 0
for i in range(n):
    lines[i] = lines[i].strip()
    split = lines[i].split(' ')
    print(split)
    ints = [int(item) for item in split]
    positive = 0
    for index, num in enumerate(ints):

        # if(NOT index==len(ints)):
        #     difference = ints[index+1]-ints[index]
        # if(difference>0):
        #     if(difference<4):
        #         positive += 1
        # else:
        #     if(difference>-4):
        #         positive -= 1
        if(index!=0):
            difference = ints[index]-ints[index-1]
            print(difference)
            if(difference>0 and difference<4):
                positive += 1
            else:
                if(difference<0 and difference>-4):
                    positive -= 1
        
        if(abs(positive)==len(ints)-1):
            total = total+1

print(f"Total={total}")
